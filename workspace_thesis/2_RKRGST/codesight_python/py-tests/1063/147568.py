casos=int(input())
while casos > 0:
    casos-=1
    a,b=map(str,input().split())
    print(int(a)%int(b))