d = 10
c = 1
for i in range (3-1):
    n=int(input())
    if n>0:
       for j in range(n-1):
           print(c,end=' ')
           c=c+d;
           d=d*10
       print(c)
       c=c+d;
       d=d*10
    else:
        print("error")
