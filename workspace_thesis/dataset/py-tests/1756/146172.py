x=int(input())
while x>0:
    y=int(input())
    j=1
    y=y%6
    for i in range(y+1):
        j=j*2
        if j>=10:
            j=j%10+j//10
    print(j)
    x-=1