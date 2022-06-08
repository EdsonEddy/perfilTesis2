n=int(input());
v=[];
for i in range(n):
    x=input();
    v.append(x[::-1])

for i in range((n-1),-1,-1):
    print(v[i]);