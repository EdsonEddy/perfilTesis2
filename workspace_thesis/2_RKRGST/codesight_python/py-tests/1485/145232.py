while True:
    x=int(input())
    c=0
    for i in range(1,x+1):
      n=input()
      
      rev=n[::-1]
       #print(rev)
      if(n==rev):
              c=c+1 
    print(c)
