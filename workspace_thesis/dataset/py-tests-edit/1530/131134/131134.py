pr=[2,3,5,7]
t=int(input())
for i in range(t):
    n=int(input())
    nn=" "
    while n>0:
        ud=n%10
        n//=10
        for j in range(4):
            if pr[j]==ud:
                nn=str(ud)+nn
    if nn==" ":
        print(0)
    else:
        print(int(nn))

