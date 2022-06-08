while True:
    try:
       n,r=map(int,input().split())
       s=0
       if  n<= 20 and n >=0:
              if  r <=50 and r >=0:
                  e = list(map(str, input().split()))
                  f=len(e)
                  f=int(f)
                  p=f
                  if n==f:
                      for i in range(0,f,1):
                            p = p-1
                            s = float(s + int(e[i]) * r ** p)
                      print(s)
    except ValueError:
        break