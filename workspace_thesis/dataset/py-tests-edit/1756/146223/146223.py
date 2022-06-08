cas=int(input())
while cas>0:
    num=int(input())
    r=1
    num=num%6
    for i in range(num+1):
        r=r*2
        if r>=10:
            r=r%10+r//10
    print(r)
    cas-=1