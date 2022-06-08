n=int(input())
a=1
for i in range(1,n+1,1):
    print('{:d}/{:d}'.format(a,i))
    if i==n:
        while a<i:
            a=a+1
            for y in range(1,n+1,1):
                print('{:d}/{:d}'.format(a,y))