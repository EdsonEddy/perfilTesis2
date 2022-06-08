c,p= map(int,input().split())
while c!= 0 or p!=0:
    rest = p - (c * 2)
    if  p>=2*c and p%2== 0 and c>=rest/2 :
          print(c - int(rest / 2), int(rest / 2))
    else: print(-1)
    c, p =map(int,input().split())