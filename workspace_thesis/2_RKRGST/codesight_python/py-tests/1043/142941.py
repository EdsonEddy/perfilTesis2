n=int(input())
while n>20 or n<0:
    n = int(input())
for i in range(n):
    r,p = map(int, input().split())
    while r>10**6 or r <0 or p>10**6 or p<0:
        r,p= map(int,input().split())
    xa=3;xb=2
    c=0
    while r>=xa and p>=xb:
        r=r-xa
        p=p-xb
        c=c+1
    s=r+p
    print(str(c)+" "+str(s))