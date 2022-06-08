def bineg(p):
    bin=""
    while p//2!=0:
        bin=str(p%2)+bin
        p=p//2
    return str(p)+bin
p=input()
h=""
for i in p:
    u=ord(i)
    d=bineg(u)


    while len(d)!= 8:
        d="0"+d
    h=h+d

print(h)