z,y,x=map(int,input().split())
if x==59:
 if y==59:
  if z==23:
   z=0
   y=0
   x=0
  else:
   z=z+1
   y=0
   x=0
 else:
  y=y+1
  x=0
else:
 x=x+1
print('%02d'%z+':''%02d'%y+':''%02d'%x) 