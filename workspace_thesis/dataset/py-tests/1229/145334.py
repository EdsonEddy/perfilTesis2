i,j=input().split()
x=len(i)
y=len(j)
if x>y:
 print(i,'>',j)
else:
 if x<y:
  print(i,'<',j)
 else:
  print(i,'=',j)