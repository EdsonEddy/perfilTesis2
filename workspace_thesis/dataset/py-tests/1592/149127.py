a=int(input())
b=input().split()
m=max(set(b), key=b.count)
r=b.count(m)
print(a-r)