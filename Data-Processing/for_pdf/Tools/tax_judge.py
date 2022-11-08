import contextlib
import sys
import numpy as np
import re
from pathlib import Path
from tqdm import tqdm
import cv2
from pikepdf import Pdf, PdfImage
import pytesseract


class DummyFile(object):
    file = None

    def __init__(self, file):
        self.file = file

    def write(self, x):
        # Avoid print() second call (useless \n)
        if len(x.rstrip()) > 0:
            tqdm.write(x, file=self.file)


@contextlib.contextmanager
def nostdout():
    save_stdout = sys.stdout
    sys.stdout = DummyFile(sys.stdout)
    yield
    sys.stdout = save_stdout


root_dir = Path('./')
pdf_list = sorted(root_dir.glob('*.pdf'))

flag1 = 0  # 有税号但没有识别到波科
flag2 = 0  # 运行失败的
flag3 = 0  # 运行失败的

for file in tqdm(list(pdf_list), file=sys.stdout):
    with nostdout():
        try:
            with Pdf.open(file) as pdf:

                page_num = len(pdf.pages)

                for ii in reversed(range(page_num)):

                    try:
                        page = pdf.pages[ii]
                        keyimage = list(page.images.keys())
                        rawimage = page.images[keyimage[0]]
                        pdfimage = PdfImage(rawimage)
                        image = pdfimage.as_pil_image()

                        if pdfimage.width / pdfimage.height < 0.6:
                            rotation_degrees = re.findall("\d+", pytesseract.image_to_osd(image).split('\n')[1])[0]
                            if rotation_degrees != '0':
                                image = image.rotate(int(rotation_degrees), expand=True)

                        elif pdfimage.width / pdfimage.height < 1.2:
                            flag3 += 1
                            continue

                        cv2_img = np.array(image)

                        # 灰度图片
                        gray = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
                        # 二值化
                        binary = cv2.adaptiveThreshold(~gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, -5)

                        rows, cols = binary.shape
                        scale = 20
                        # 自适应获取核值 识别横线
                        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (cols // scale, 1))
                        eroded = cv2.erode(binary, kernel, iterations=1)
                        dilated_col = cv2.dilate(eroded, kernel, iterations=1)


                        # 识别竖线
                        scale = 20
                        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, rows // scale))
                        eroded = cv2.erode(binary, kernel, iterations=1)
                        dilated_row = cv2.dilate(eroded, kernel, iterations=1)


                        # 标识交点
                        bitwise_and = cv2.bitwise_and(dilated_col, dilated_row)

                        # 
                        # 识别黑白图中的白色交叉点，将横纵坐标取出
                        ys, xs = np.where(bitwise_and > 0)

                        # print(ys, xs)
                        # 纵坐标
                        y_point_arr = []
                        # 横坐标
                        x_point_arr = []
                        # 通过排序，获取跳变的x和y的值，说明是交点，否则交点会有好多像素值值相近，我只取相近值的最后一点
                        # 这个10的跳变不是固定的，根据不同的图片会有微调，基本上为单元格表格的高度（y坐标跳变）和长度（x坐标跳变）
                        i = 0
                        sort_x_point = np.sort(xs)

                        for i in range(len(sort_x_point) - 1):
                            if sort_x_point[i + 1] - sort_x_point[i] > 20:
                                x_point_arr.append(sort_x_point[i])
                            i = i + 1
                        x_point_arr.append(sort_x_point[i])  # 要将最后一个点加入

                        i = 0
                        sort_y_point = np.sort(ys)

                        for i in range(len(sort_y_point) - 1):
                            if (sort_y_point[i + 1] - sort_y_point[i] > 60):
                                y_point_arr.append(sort_y_point[i])
                            i = i + 1

                        # 要将最后一个点加入
                        y_point_arr.append(sort_y_point[i])

                        # 来个范围筛选
                        for i in range(len(x_point_arr)):
                            if x_point_arr[i] > 100:
                                break

                        for j in range(len(y_point_arr)):
                            if y_point_arr[j] > 300:
                                j = j - 1
                                break
                            elif y_point_arr[j] > 100:
                                break

                        img = image.crop((x_point_arr[i+1], y_point_arr[j+1], x_point_arr[i+6], y_point_arr[j+2]))

                        text = pytesseract.image_to_string(img, lang='chi_sim')

                        # reg_tax = r'913\d*'
                        reg_tax = r'91[0-9A-Za-z]*'
                        # reg_tax2 = r'[纳税人识别号].*?(\d+)'
                        reg_com = r'波科|国际|医疗'
                        tax_real = '913100006073791417'

                        tax_reco_s = re.findall(reg_tax, text)
                        # tax_reco_s2 = re.findall(reg_tax2, text)
                        com_reco_s = re.findall(reg_com, text)

                        # 发现有税号页
                        if tax_reco_s:
                            tax_reco = tax_reco_s[0]
                            if tax_reco != tax_real: 
                                # 且是波科的
                                if com_reco_s:
                                    print(f'{file.stem} 的第[{ii+1}]页有税号错误, {tax_reco}')
                                    break
                                else:
                                    # print(f'{file.stem} 的第[{ii+1}]页有不是波科的')
                                    flag1 += 1

                    except Exception as ex:
                        # print(f'{file.stem} 的第[{ii+1}]页运行失败, 错误：{ex}')
                        img = image.crop((0, 0, image.size[0] / 1.8, image.size[1] / 2))
                        text = pytesseract.image_to_string(img, lang='eng+chi_sim')

                        # reg_tax = r'913\d*'
                        reg_tax = r'91[0-9A-Za-z]*'
                        # reg_tax2 = r'[纳税人识别号].*?(\d+)'
                        reg_com = r'波科|国际|医疗'
                        tax_real = '913100006073791417'

                        tax_reco_s = re.findall(reg_tax, text)
                        # tax_reco_s2 = re.findall(reg_tax2, text)
                        com_reco_s = re.findall(reg_com, text)

                        # 发现有税号页
                        if tax_reco_s:
                            tax_reco = tax_reco_s[0]
                            if tax_reco != tax_real: 
                                # 且是波科的
                                if com_reco_s:
                                    print(f'{file.stem} 的第[{ii+1}]页有税号错误, {tax_reco}')
                                    break
                                else:
                                    # print(f'{file.stem} 的第[{ii+1}]页有不是波科的')
                                    flag1 += 1
                        
        except Exception as ex:
            flag2 += 1
            # print(f'{file.stem} 的第[{ii+1}]页运行失败, 错误：{ex}')
            pass


print('flag1:', flag1, 'flag2:', flag2, 'flag3:', flag3)