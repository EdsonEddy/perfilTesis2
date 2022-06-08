n=int(input())
c=1
while c<=n:
 a,b=map(int,input().split())
 if a<=b:
  men=a
  may=b
 else:
  men=b
  may=a
 while men>0:
  may,men=men,may%men
 print(may)
 c=c+1