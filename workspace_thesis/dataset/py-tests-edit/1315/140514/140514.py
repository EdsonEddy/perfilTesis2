from sys import stdin, stdout
n = input()
n = int(n)
x = input()
v = x.split(" ")
for i in range(n):
    v[i] = int(v[i])
print(v[0], end = "")
for i in range(1,n):
    print("",(v[i] - v[i-1]), end="")
print("")