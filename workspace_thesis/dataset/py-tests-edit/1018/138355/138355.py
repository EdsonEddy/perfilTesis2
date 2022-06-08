N=int(input())
while (N>0):
    N1,N2=map(int,input().split())
    #N2=int(input())
    if(N1>N2):
        print(">")
    elif (N1<N2):
        print ("<")
    else:
        print("=")
    N=N-1
