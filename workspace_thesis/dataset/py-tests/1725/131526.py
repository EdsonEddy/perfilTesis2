while True:
    try:
      k,t=map(int,input().split())
      c=0
      p=0
      l=0
      mult=0
      sum=0
      if k >= 80 and k <= 160:
          if t >= 80 and  t <= 163800:
              while sum !=t:
                   c=c+1
                   p=2**l
                   mult=k*p
                   l=l+1
                   sum=sum+mult
              print(c)
    except ValueError:
        break