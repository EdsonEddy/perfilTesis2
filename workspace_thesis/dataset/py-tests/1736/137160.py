n=int(input())
i=0
while i<n:
    if i==n-1:
       f=int((2**(2**i))+1)
       print (f,end="")  
    else:   
       f=int((2**(2**i))+1)
       print (f,end=" ")
    i=i+1