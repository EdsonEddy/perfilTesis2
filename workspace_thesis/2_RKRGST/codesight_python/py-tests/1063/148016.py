c=int(input())
for i in range(c):
    m,a=map(int,input().split())
    while m<1 or m>10**10**6 and a<1 or a>1000:
        m,a=map(int,input().split())
    print(m%a)