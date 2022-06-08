def alvaro(s):
    r="ABC"
    c=0
    n=len(s)
    res=0
    for i in range(n):
        if s[i]==r[c]:
            res+=1
        c+=1
        if c==3:
            c=0
    return res
def edwin(s):
    r="BABC"
    c=0
    n=len(s)
    res=0
    for i in range(n):
        if s[i]==r[c]:
            res+=1
        c+=1
        if c==4:
            c=0
    return res
def gabriel(s):
    r="CCAABB"
    c=0
    n=len(s)
    res=0
    for i in range(n):
        if s[i]==r[c]:
            res+=1
        c+=1
        if c==6:
            c=0
    return res

while True:
    p=int(input())
    s=str(input())
    n1=alvaro(s)
    n2=edwin(s)
    n3=gabriel(s)
    m=max(n1,n2,n3)
    print(m)
    if m==n1:
        print("Alvaro")
    if m==n2:
        print("Edwin")
    if m==n3:
        print("Gabriel")