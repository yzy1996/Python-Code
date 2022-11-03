import contextlib
import sys

import re
from pathlib import Path
from tqdm import tqdm

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

for file in tqdm(list(pdf_list), file=sys.stdout):
    with nostdout():
        try:

            with Pdf.open(file) as pdf:

                page_num = len(pdf.pages)

                for i in reversed(range(page_num)):
                    page = pdf.pages[i]
                    keyimage = list(page.images.keys())
                    rawimage = page.images[keyimage[0]]
                    pdfimage = PdfImage(rawimage)
                    img = pdfimage.as_pil_image()

                    if pdfimage.width / pdfimage.height < 0.6:
                        rotation_degrees = pytesseract.image_to_osd(img).split('\n')[1][-2:]
                        if rotation_degrees != '0':
                            img = img.rotate(int(rotation_degrees),expand=True)

                    elif pdfimage.width / pdfimage.height < 1.2:
                        continue

                    img = img.crop((400, img.size[1] / 5, img.size[0] / 1.8, img.size[1] / 2))

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
                        # 且是波科的
                        if com_reco_s:
                            tax_reco = tax_reco_s[0]
                            if tax_reco != tax_real:
                                print(f'{file.stem} 的第[{i+1}]页有税号错误, {tax_reco}')
                                break
                        else:
                            flag1 += 1
        except Exception as ex:
            flag2 += 1
            print(f'{file.stem} 的第[{i+1}]页运行失败, 错误：{ex}')
            pass

print('flag1:', flag1, 'flag2:', flag2)