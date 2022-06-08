X=int(input())
for i in range(X):
    A,B=map(int,input().split(" "))
    A1=0
    if A>B:
        while A1<=A:
            A1=A1+1
            if A%A1==0 and B%A1==0:
                M=A1
    else:
        while A1<B:
            A1=A1+1
            if A%A1==0 and B%A1==0:
                M=A1
    print(M)