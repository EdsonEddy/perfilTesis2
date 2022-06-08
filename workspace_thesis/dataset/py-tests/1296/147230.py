n = int(input())
l= []
for i in range(n):
    w = input()
    i = w[::-1]
    l.append(i)
for j in range(len(l)):
    print(l.pop())
