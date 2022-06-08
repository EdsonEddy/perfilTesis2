n=0
while n!="":
    n=int(input())
    x=bin(n)
    y=str(x)[2:]
    c=y[::-1]
    print(int(c,2))