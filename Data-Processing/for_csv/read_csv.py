'''
读取csv，csv示例如下：

Symbol,Price,Date,Time,Change,Volume
"AA",39.48,"6/11/2007","9:36am",-0.18,181800
"AIG",71.38,"6/11/2007","9:36am",-0.15,195500
"AXP",62.58,"6/11/2007","9:36am",-0.46,935000
"BA",98.31,"6/11/2007","9:36am",+0.12,104800
"C",53.08,"6/11/2007","9:36am",-0.25,360900
"CAT",78.29,"6/11/2007","9:36am",-0.23,225400

方式1、读取为单行元组
row[0] 就会是 AA

方式2、数据存储格式为 DataFrame
'''

# import csv

# with open('test.csv') as f:
#     f_csv = csv.reader(f)
#     headers = next(f_csv)  # headers E
#     print(f_csv[0][0])
#     # for row in f_csv:
#     #     print(row[0])

import pandas

f_csv = pandas.read_csv('test.csv')

print(f_csv['Price'][0])