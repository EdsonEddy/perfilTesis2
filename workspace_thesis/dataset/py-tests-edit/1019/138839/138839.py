t=int(input())
for i in range(1,t+1):
    R=lambda:map(int,input().split())
    a,b,c=R()
    v=[a,b,c]
    v.sort()
    print("Case "+str(i)+": "+str(v[1]))