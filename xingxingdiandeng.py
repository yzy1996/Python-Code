
#coding: utf-8
def xingxing(N):
    for i in range(N):
        j=i+1
        if j==1:
            print(' '*(N-1)+'*'+' '*(N-1))
        elif j<N:
            print(' '*(N-j)+'*'+(2*j-3)*'#'+'*'+' '*(N-j))
        else:
            print((2*N-1)*'*')


xingxing(10)
