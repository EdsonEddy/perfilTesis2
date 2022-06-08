n=int(input())
i=1
while (i<=n):
                   a=1
                   b=0
                   j=1
                   x=int(input())
                   while (j<=x):
                                      c=a+b
                                      a=b
                                      b=c
                                      j=j+1
                   print (c)
                   i=i+1