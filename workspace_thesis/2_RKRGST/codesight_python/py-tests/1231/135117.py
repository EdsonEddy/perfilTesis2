h, m, s= map(int, input().split())
s=s+1
if(s==60):
    m=m+1
    s=0
    if(m==60):
        h=h+1
        m=0
        if(h==24):
            h=0
if(h>9):
    print(str(h)+":",end="")
else:
    print("0"+str(h)+":",end="")
if(m>9):
    print(str(m) + ":", end="")
else:
    print("0" + str(m) + ":", end="")
if(s>9):
    print(str(s))
else:
    print("0" + str(s))