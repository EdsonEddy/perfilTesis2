import sys
for case in sys.stdin:
    f,s=map(int,case.split())
    i=1
    c=0
    while True:
        c+=1
        y=(int((f+i)/2))
        if y==s:
            break
        if y<s:
            i=(y+1)
        else:
            f=(y-1)
    print(c)
