def st(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]
s=str(input())
bulbasur=st(s)
for x in bulbasur:
    print (x,end='')