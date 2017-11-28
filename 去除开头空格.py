for i in range(10):
    for j in range(10):
        str1='C:\\Users\\Jerry\\Desktop\\语音识别\\数据集\\'+ str(i) +'_'+str(j)+'.txt'
        str2='C:\\Users\\Jerry\\Desktop\\语音识别\\'+str(i)+'_'+str(j)+'.txt'
        with open(str1,'r') as fr,open(str2,'w') as fw:
            for line in fr.readlines():
                fw.write(line.lstrip())