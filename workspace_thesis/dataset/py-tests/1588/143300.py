n= int(input())
g= 0
for j in range(n):
    o = int(input())
    g = 0
    s= input().split()
    for i in s:
        u = int(i)
        if u%3==0:
            g = g+u
    y = g*2
    print("La suma es",y)



