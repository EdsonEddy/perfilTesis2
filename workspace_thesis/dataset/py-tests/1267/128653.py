while True:
    try:
       n=int(input())
       if n==-1:
           break
       elif 0<=n and n <=1000:
           n=(n*2)+1
           print(n)
    except ValueError:
        break