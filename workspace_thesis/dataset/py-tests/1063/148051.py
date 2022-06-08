n = int(input())
while n>0:
    a,m = input().split()
    a = int(a)
    m = int(m)
    #a=651838061
    #m = 99
    c = a%m
    print(c)
    n-=1