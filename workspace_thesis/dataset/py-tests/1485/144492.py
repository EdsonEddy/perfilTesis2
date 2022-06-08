while True:
    s=int(input())
    c=0
    for i in range(s):
        a=input()
        if a==a[::-1]:
            c=c+1
    print(c)