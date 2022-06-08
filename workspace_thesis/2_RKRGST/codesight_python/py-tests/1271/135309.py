x=int(input())
s=0
for i in range(x):
   n=int(input())
   aux=n
   while n>0:
      dig=n-(n//10)*10
      n=n//10
      fac=1
      for j in range(1,dig+1):
         fac=fac*j
      s=s+fac
   if aux==s:
      print("Y")
      s=0
   else:
      print("N")
      s=0   