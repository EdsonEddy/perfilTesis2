def binex(u):
    bin=""
    while u//2!=0:
        bin=str(u%2)+bin
        u=u//2
    return str(u)+bin
u=input()
r=""
for i in u:
    j=ord(i)
    t=binex(j)


    while len(t)!= 8:
        t="0"+t
    r=r+t

print(r)

