n=int(input())
while n<1 or n>10:
    n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    while x<1 or x>10**10**6 and y<1 or y>1000:
        x,y=map(int,input().split())
    print(x%y)
