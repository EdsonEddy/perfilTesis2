n=int(input())
while 0<n:
    m=int(input())
    c=1
    m=m%6
    for i in range(m+1):
        c=c*2
        if c>=10:
            c=c%10+c//10
        #else:
            #print()
    print(c)
    m-=1