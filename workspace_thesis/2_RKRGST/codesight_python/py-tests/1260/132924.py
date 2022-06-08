n = int(input())
for i in range (n):
    a, b = map(int, input().split(" "))
    aux = 0
    for j in range (1,b):
        if a % j == 0 and b % j == 0:
            aux = j
    print (aux)