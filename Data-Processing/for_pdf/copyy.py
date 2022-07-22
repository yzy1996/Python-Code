import re
import os
from pathlib import Path
import subprocess
from tqdm import tqdm
import shlex

from pikepdf import Pdf, PdfImage
from pyzbar.pyzbar import decode

from collections import Counter

root_dir = Path('./')
pdf_list = sorted(root_dir.glob('scan*.pdf')) + sorted(root_dir.glob('image*.pdf'))

# 先将 pdf 页面转 image，再用 pyzar 去直接识别二维码得到 Code
def zbar_read(filename):

    with Pdf.open(filename) as pdf:

        page = pdf.pages[0] # [0:3]
        keyimage = list(page.images.keys())
        rawimage = page.images[keyimage[0]]
        pdfimage = PdfImage(rawimage)

        decoded_data = decode(pdfimage.as_pil_image())

        if decoded_data:
            QR_data = decoded_data[0].data.decode()
            CR_check = re.findall(r'CR-[A-Z]{2,3}-\d{4}-\d{4}', QR_data)
            scan_CR = CR_check[0] if CR_check else []
        else:
            scan_CR = [] 

    return scan_CR

    
def ocrmypdf_read(filename, try_count=1):

    if try_count == 1:
        command = f"ocrmypdf --quiet --pages 1 --optimize 0 --output-type none --sidecar ocr_output.txt {filename} -"
    if try_count == 2:
        command = f"ocrmypdf --quiet --deskew --rotate-pages --rotate-pages-threshold 2 --pages 1,2,3 --optimize 0 --output-type none --sidecar ocr_output.txt {filename} -"

    command_args = shlex.split(command)

    with open('log', "w") as outfile:
        subprocess.run(command_args, stdout=outfile)
    os.remove('log')

    output_file = Path('ocr_output.txt')
    content = output_file.read_text(encoding='utf-8')
    output_file.unlink()

    # 正则表达式 匹配类似 CR-UR-2206-3288，已经加上三位的
    scan_CR_L = re.findall(r'CR-[A-Z]{2,3}-\d{4}-\d{4}', content)

    scan_CR = scan_CR_L[-1] if scan_CR_L else []

    return scan_CR

count_total = []

for file in tqdm(list(pdf_list)):

    # 记录尝试次数
    try_count = 0

    # 第一次使用 zbar 识别
    try:
        scan_CR = zbar_read(file)

    except:
        try_count += 1
        count_total.append(try_count)
        continue

    # if not scan_CR:
    #     try_count += 1
    #     # 第二次使用 OCR 识别 
    #     scan_CR = ocrmypdf_read(file, try_count)

    #     if not scan_CR:
    #         try_count += 1
    #         # 第三次使用更复杂的 OCR 识别 
    #         scan_CR = ocrmypdf_read(file, try_count)

    #         if not scan_CR:
    #             try_count += 1
    #             count_total.append(try_count)
    #             continue

    if not scan_CR:
        try_count += 1
        count_total.append(try_count)
        continue


    if not file.with_stem(scan_CR).exists():
        file.rename(file.with_stem(scan_CR))

    # 重复命名的问题
    else:
        num = 2
        while file.with_stem(scan_CR + f'({num})').exists():
            num += 1
        else:
            file.rename(file.with_stem(scan_CR + f'({num})'))

    count_total.append(try_count)

count_dict = Counter(count_total)

print('成功:', count_dict.get(0, 0), 
      '| 失败:', count_dict.get(1, 0))