n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    s=[1]*b

    for i in range(a):

        s[i%b]=sum(s)
    print(s[a%b])