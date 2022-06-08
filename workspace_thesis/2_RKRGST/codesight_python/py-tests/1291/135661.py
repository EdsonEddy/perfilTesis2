import sys
for x in sys.stdin:
    sum=0
    lis=list(map(int,x.split()))
    for i in lis:
        sum=sum+i
    print(sum)
