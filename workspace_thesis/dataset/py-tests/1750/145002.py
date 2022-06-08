while(True):
    x=input()
    j=2
    k=2
    j1=4
    m=0
    flag=False
    for i in range(len(x)):
        if m!=1:
            z=i+j
        else:
            z=n
        if x[:k]==x[z:i+j1]:
            k=k+1
            m=1
            n=z
            if i+3==len(x)-1:
                flag=True
    if flag==True:
        print("si")
    else:
        print("no")