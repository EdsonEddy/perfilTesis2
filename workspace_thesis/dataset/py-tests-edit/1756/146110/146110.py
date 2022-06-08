casos=int(input())
while casos>0:
    num=int(input())
    l=1
    num=num%6
    for i in range(num+1):
        l=l*2
        if l>=10:
            l=l%10+l//10
    print(l)
    casos-=1