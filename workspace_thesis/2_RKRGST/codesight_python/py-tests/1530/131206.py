y = int(input())
pr=[2,3,5,7]
for i in range(y):
    n = int(input())
    nn=" "
    while(n>0):
        x=n%10
        n=n//10
        for j in range(4):
            if pr[j]== x:
                nn=str(x)+nn
    if(nn==" "):
        print (0)

    else:
        print (int(nn))