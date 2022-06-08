from sys import*
for line in stdin:
    n,k=map(int,line.split())
    if (n+1)//2<k:
        print(abs(((n+1)//2)-k)*2)# abs((n+1)-2k)
    else:
        print(2*k-1)