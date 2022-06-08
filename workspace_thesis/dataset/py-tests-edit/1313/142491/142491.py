import sys
def busca(a,lst):
    s=0
    c=0
    for i in range(0,a):
        x=lst[i]
        for j in range(0,a):
            b=lst[j]
            if b>=x:
                s=s+1
        s=s*x
        if s>c:
            c=s
        s=0
    return c


for a in sys.stdin:
    a=int(a)
    lst = input().split()
    lst = [int(ch) for ch in lst]
    print(busca(a,lst))
