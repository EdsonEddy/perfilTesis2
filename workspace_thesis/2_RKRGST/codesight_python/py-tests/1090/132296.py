n=int(input())
s=0
if n>=1 and n<=10000:
    for i in range (3,n,3):
        s=s+i
    print (s)    