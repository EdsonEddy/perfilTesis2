n=int(input())
for i in range(0,n,1):
    a, b=map(int, input().split(" "))
    resto = 0
    while b > 0:
     resto = b
     b = a % b
     a = resto
     s = a
    print(s)