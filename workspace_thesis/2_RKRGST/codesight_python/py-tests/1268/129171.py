n=1
while(n==1):
    c,p=map(int,input().split())
    if c==0 and p==0:
        break
    else:
        if(p%2!=0) or (c*4<p) or (c>p):
            print(-1)
        else:
           y=(p-2*c)//2
           x=(4*c-p)//2
           if x<0 or y<0:
               print(-1)
           else:
               print(x,y)