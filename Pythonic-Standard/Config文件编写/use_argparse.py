'''argparse --- 命令行选项、参数和子命令解析器
argparse 模块可以让人轻松编写用户友好的命令行接口。
程序定义它需要的参数，然后 argparse 将弄清如何从 sys.argv 解析出那些参数。 
argparse 模块还会自动生成帮助和使用手册，并在用户给程序传入无效参数时报出错误信息。
'''

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--echo')
args, unknown = parser.parse_known_args()
print(args, unknown)

