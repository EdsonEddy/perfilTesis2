import math
while True:
    j=input()
    if j=="":
        break
    R=lambda:map(int,j.split())
    '''R=lambda:map(int,input().split())'''
    base,num,=R()
    g=math.log10(num)
    h=math.log10(base)
    res=int(g/h)
    
    print(res)