import sys
for l in sys.stdin:
    a=list(map(int,l.split()))
    i=0
    s=0
    while a[i]!=0:
     s=s+a[i]
     i=i+1
    print(s)
