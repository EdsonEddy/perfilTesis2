q=int(input())
while q>0:
    numer=int(input())
    r=1
    numer=numer%6
    for i in range(numer+1):
        r=r*2
        if r>=10:
            r=r%10+r//10
    print(r)
    q-=1