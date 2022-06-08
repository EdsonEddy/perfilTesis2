a,b=map(int,input().split())
n=int(input())
l = input().split()
res=0
for i in l:
    if int(i)>=a and int(i)<=b:
        res+=int(i)
print(res)