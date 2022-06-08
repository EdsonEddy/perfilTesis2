import sys

def extremo(a, lst):
        c=0
        for i in range(1, a-1):
            v=lst[i]
            a=lst[i-1]
            b=lst[i+1]
            if (a>v and b>v)or(v>a and v>b):
                c=c+1
        return c
    
for a in sys.stdin:
    a=int(a)
    lst = input().split()
    lst = [int(ch) for ch in lst]
    print(extremo(a, lst))