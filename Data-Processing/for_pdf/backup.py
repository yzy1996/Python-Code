import re
import os
from pathlib import Path
import subprocess
import ocrmypdf


## TODO: 1. 解决颠倒问题
if __name__ == '__main__':
        
    # Step1: 读取根目录下的 pdf 文件列表
    root_dir = Path('./')
    pdf_list = root_dir.glob('scan*.pdf')

    # 设置匹配 CR-UR-2206-3288 的正则表达式，加上三位的
    re_text = r'CR-[A-Z]{2,3}-\d{4}-\d{4}'

    # Step2: 开始挨个处理
    for file in pdf_list:

        # 执行OCR，产生 ocr_output.txt
        # command = f"ocrmypdf --pages 1 --optimize 0 --output-type none --sidecar ocr_output.txt {file} -"
        # subprocess.run(command, shell=True, stdout=subprocess.DEVNULL)

        ocrmypdf.ocr(file, '-', deskew=True, sidecar='ocr_output.txt', pages=1, optimize=0, output_type=None)

        with open('ocr_output.txt', 'r', encoding='utf-8') as f:

            content = f.read()

            try:
                scan_CR = re.findall(re_text, content)[0]

            except:
                print('#---', file.name, '识别异常! 请手动处理', '---#')
                continue

            # 重命名
            name_str = scan_CR + '.pdf'
            new_name = root_dir / name_str

            if not new_name.exists():
                file.rename(new_name)
                print('#---', file.name, '已修改为', name_str, '---#')
            else:
                print('#---', file.name, '文件已存在! 请手动处理', '---#')

    # os.remove("ocr_output.txt")  
