import pandas as pd

sales=pd.read_csv('train_data.csv',sep='\s*,\s*',engine='python')  #读取CSV
X=sales['X'].values    #存csv的第一列
Y=sales['Y'].values    #存csv的第二列

#初始化赋值
s1 = 0
s2 = 0
s3 = 0
s4 = 0
n = 4       ####你需要根据的数据量进行修改

#循环累加
for i in range(n):
	s1 = s1 + X[i]*Y[i]
	s2 = s2 + X[i]
	s3 = s3 + Y[i]
	s4 = s4 + X[i]*X[i]
	
#计算斜率和截距
b = (s2*s3-n*s1)/(s2*s2-s4*n)
a = (s3 - b*s2)/n
print("Coeff: {} Intercept: {}".format(b, a))

