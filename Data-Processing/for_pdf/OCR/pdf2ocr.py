import os
import subprocess
import shlex

file = '2.pdf'
command = f"ocrmypdf --deskew --rotate-pages --rotate-pages-threshold 5 --output-type none --sidecar ocr_output.txt {file} -"
command_args = shlex.split(command)

with open('log', "w") as outfile:
    subprocess.run(command_args, stdout=outfile)
os.remove('log')