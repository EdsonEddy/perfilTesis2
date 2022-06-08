def str2bits(a=''):
    return [bin(ord(i))[2:].zfill(8) for i in a]
a=str(input())
d=str2bits(a)
for i in d:
    print (i,end='')