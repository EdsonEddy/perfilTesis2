n=int(input())
for i in range(n):
    x=int(input())
    a=1
    x=x%6
    for j in range(x+1):
        a=a*2
        if a>=10:
            a=a%10+a//10
    print(a)
