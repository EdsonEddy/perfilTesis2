n=int(input())
pi='3.141592653589793238462643383279502'
if n==0:
    print(pi[0])
else:
    f=(pi[:n+1])
    if int(pi[n+2])<5:
        g=int(pi[n+1])
    else:
        g=int((pi[n+1]))+1
    h=f+str(g)
    print(h)