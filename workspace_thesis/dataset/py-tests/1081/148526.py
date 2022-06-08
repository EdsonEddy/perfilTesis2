def primo(n):
    r=int(n**(0.5))+1
    for i in range(2,r):

        if p[i]==0:
            for j in range(i+i,n,i):
                p[j]=1

p=[0]*100000
primo(100000)
x=int(input())
for j in range(x):

    n=int(input())

    h=n
    l=n

    if p[h]==0:
        print('0')

    else:
        while p[l]!=0 and p[h]!=0:
            l=l+1
            h=h-1
        print(n-h)
