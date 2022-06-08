a,b=map(int,input().split())#
cad1=input()
cad2=input()
v=list(map(int,cad1.split()))
v1=list(map(int,cad2.split()))
for i in range(len(v1)):
    if v.count(v1[i])==0:
        v.append(v1[i])
v.sort()
for i in range(len(v)):
    print(v[i])
