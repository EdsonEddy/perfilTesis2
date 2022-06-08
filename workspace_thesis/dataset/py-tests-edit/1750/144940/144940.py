import sys
for lst in sys.stdin:
    lst=(lst)
    a=lst
    l=len(a)-1
    b=(l//2)-1
    d=a[0:b+1]
    c=a[b+1:l]
    if d==c:
        print("si")
    else:
        print("no")