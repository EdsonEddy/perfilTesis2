def str2bits(x=''):
    return [bin(ord(j))[2:].zfill(8) for j in x]
x=str(input())
k=str2bits(x)
for j in k:
    print (j,end='')