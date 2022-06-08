n = int(input())
A = []
c = input()
c = c.split(" ")
for i in range(n):
    A.append(int(c[i]))
V = []
for i in range(n):
    if i==0:
        V.append(int(c[0]))
    else:
        V.append(A[i]-A[i-1])
    if i==n-1:
        print(V[i],end="")
    else:
        print(V[i],end=" ")