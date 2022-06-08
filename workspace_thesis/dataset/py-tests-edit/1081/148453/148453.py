def primo(n):
    r=int(n**(0.5))+1
    for i in range(2,r):

        if p[i]==0:
            for j in range(i+i,n,i):
                p[j]=1
x=int(input())
p=[0]*100000
primo(100000)


for j in range(x):

    n=int(input())

    h=n
    l=n

    if p[h]==0:
        print('0')

    else:
        for i in range(1,n):

            l=l+1
            h=h-1
            if p[h]==0 or p[l]==0:
                print(i)
                break
