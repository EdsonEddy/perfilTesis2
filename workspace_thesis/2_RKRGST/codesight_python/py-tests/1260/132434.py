n = int(input())
for i in range (1,n+1,1):
    a, b = map(int,input().split(" "))
    while b:
        mcd=b
        b=a%b
        a=mcd
    print(mcd)
