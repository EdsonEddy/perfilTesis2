x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    if b>=0 and a**b<=2**62:
        print(a**b)
        
