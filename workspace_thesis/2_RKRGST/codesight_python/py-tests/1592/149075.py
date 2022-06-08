n=int(input())
z=input().split()
num=max(set(z), key=z.count)
p=z.count(num)
x = n - p
print(x)