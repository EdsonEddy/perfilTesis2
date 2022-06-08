t=int(input())
n = 1
while n <= t:
    R=lambda:map(int,input().split())
    a,b,c=R()
    vec=[a,b,c]
    vec.sort()
    
    print("Case "+str(n)+": "+str(vec[1]))
    n += 1