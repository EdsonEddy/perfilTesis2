n=int(input())
v=[]
for i in range(n):
    x=input()
    cad=x[::-1]
    v.append(cad)
    cad=""
v=v[::-1]
for j in range(n):
    print(v[j])