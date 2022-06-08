a,b = map(int, input().split())
cad1=input()
cad2=input()
v=list(map(int,cad1.split()))
v1=list(map(int,cad2.split()))
v2=v+v1
v2.sort()
v2.append(" ")
for i in range(len(v2)-1):
    if v2[i+1]!=v2[i]:
        print(v2[i])
            