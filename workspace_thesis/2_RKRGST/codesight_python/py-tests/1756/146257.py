ap=int(input())
for i in range(ap):
    num=int(input())
    a=1
    num=num%6
    for i in range(num+1):
        a=a*2
        if a>=10:
            a=a%10+a//10
    print(a)
