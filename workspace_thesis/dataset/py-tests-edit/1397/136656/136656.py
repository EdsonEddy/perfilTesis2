def decimal(bin):
    bin = str(bin)
    num = int(bin,2)
    return num
while True:
    n = int(input())
    c,l,s = 0,[],0
    if n == 1:
        l.append(3)
    elif n ==2:
        l.append(3)
        l.append(5)
    for i in range(0,n):
        for c in range(0,i):
            s = (10**c)+(10**i)
            c += 1        
            l.append(decimal(s))
    for i in range(0,n):
        if i != n-1:
            print(l[i],end=' ')
        else:
            print(l[i])