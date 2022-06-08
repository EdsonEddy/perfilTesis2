def fibo(j):
    a=1
    b=0
    for i in range(1,j+1):
      c=a+b
      a=b
      b=c
    print(c)

      
def par(m):
    a=2
    c=0
    for i in range(1,m+1):
        c=c+a
    print(c)   



n=int(input())
j=1
m=1
for i in range(1,n+1):
   if i%2!=0:
       fibo(j)
       j=j+1

   else:
        par(m)
        m=m+1       

  