while True:
    c=int(input())
    r=0
    for i in range(c):
        a=input()
        pal=a[::-1]
        if a==pal:
            r=r+1
    print(r)