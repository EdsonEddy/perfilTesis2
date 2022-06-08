N=int(input())
while (N>0):
    N=N-1
    n = int(input())
    if(n>2):
        a = b = 1
        i = 2
        while(i<n):
            f = a + b
            a = b
            b = f
            i = i + 1
        print(b)
    else:
        print(1)
