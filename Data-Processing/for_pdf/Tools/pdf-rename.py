import re
import os
from pathlib import Path
import subprocess
from tqdm import tqdm
import shlex

from pikepdf import Pdf, PdfImage
from pyzbar.pyzbar import decode


def zbar_read(filename, page_num=0):

    with Pdf.open(filename) as pdf:

        page = pdf.pages[page_num] # [0:3]
        keyimage = list(page.images.keys())
        rawimage = page.images[keyimage[0]]
        pdfimage = PdfImage(rawimage)

        decoded_data = decode(pdfimage.as_pil_image())

        if decoded_data:
            QR_data = decoded_data[0].data.decode()
            scan_CR_L = re.findall(r'CR-[A-Z]{2,3}-\d{4}-\d{4}', QR_data)
            scan_CR = scan_CR_L[0] if scan_CR_L else []
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

def rename(file, scan_CR):

    if not file.with_stem(scan_CR).exists():
        file.rename(file.with_stem(scan_CR))

    # 重复命名的问题
    else:
        num = 2
        while file.with_stem(scan_CR + f'({num})').exists():
            num += 1
        else:
            file.rename(file.with_stem(scan_CR + f'({num})'))


def try1():

    root_dir = Path('./')
    pdf_list = sorted(root_dir.glob('scan*.pdf')) + \
               sorted(root_dir.glob('image*.pdf'))

    fail_count = 0

    for file in tqdm(list(pdf_list)):

        try:
            scan_CR = zbar_read(file, 0)

            if not scan_CR:
                fail_count += 1
                continue
            
            rename(file, scan_CR)

        except:
            fail_count += 1
            continue

    print('方法1失败:', fail_count)

def try2():

    root_dir = Path('./')
    pdf_list = sorted(root_dir.glob('scan*.pdf')) + \
               sorted(root_dir.glob('image*.pdf'))

    fail_count = 0

    for file in tqdm(list(pdf_list)):

        try:
            scan_CR = zbar_read(file, 1)

            if not scan_CR:
                fail_count += 1
                continue
            
            rename(file, scan_CR)

        except:
            fail_count += 1
            continue

    print('方法2失败:', fail_count)

def try3():

    root_dir = Path('./')
    pdf_list = sorted(root_dir.glob('scan*.pdf')) + \
               sorted(root_dir.glob('image*.pdf'))

    fail_count = 0

    for file in tqdm(list(pdf_list)):

        try:
            scan_CR = ocrmypdf_read(file, 1)

            if not scan_CR:
                fail_count += 1
                continue
            
            rename(file, scan_CR)

        except:
            fail_count += 1
            continue
    
    print('方法3失败:', fail_count)


def try4():

    root_dir = Path('./')
    pdf_list = sorted(root_dir.glob('scan*.pdf')) + \
               sorted(root_dir.glob('image*.pdf'))

    fail_count = 0

    for file in tqdm(list(pdf_list)):

        try:
            scan_CR = ocrmypdf_read(file, 2)

            if not scan_CR:
                fail_count += 1
                continue
            
            rename(file, scan_CR)

        except:
            fail_count += 1
            continue
    
    print('方法4失败:', fail_count)


if __name__ == "__main__":
    try1()
    try2()
    try3()
    try4()


