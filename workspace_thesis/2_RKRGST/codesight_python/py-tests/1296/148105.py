p = int(input())
l = [0]*p
for i in range(p):
    l[i] = input()
for i in range(p-1, -1, -1):
    print(l[i][::-1])