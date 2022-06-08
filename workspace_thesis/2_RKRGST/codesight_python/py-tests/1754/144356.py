while True:
    s=str(input())
    a=len(s)
    c=0
    for d in range(0,a-1,1):
        if s[d]==s[d+1]:
            if s[d]!="r" and s[d]!="l":
                c=1
    if c>0:
        print("si")
    else:
        print("no")
