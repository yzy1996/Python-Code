'''
一个生成金字塔的代码，根据你输入的层数显示出来
'''

a=input("Enter N = ")
b=int(a)
for i in range(b-1):
    print(" ",end='')
print("*",end='')
print("\n")

for i in range(1,b-1):
    for j in range(b-i-1):
        print(" ",end='')
    print("*",end='')
    for l in range(2*i-1):
        print("#",end='')
    print("*",end='')
    print("\n")
	
if b>1:
    for i in range(2*b-1):
        print("*",end='')