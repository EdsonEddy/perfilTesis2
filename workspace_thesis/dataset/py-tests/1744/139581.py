n = int(input())
espacios = 0
i = 1
while n > 0:
    for j in range(1,n+1):
        print(j,end="")
    for j in range(1, espacios):
        print(" ",end="")
    for j in range(n-i, 0, -1):
        print(j, end="")
    print()
    i=0
    n = n-1
    espacios = espacios+2
