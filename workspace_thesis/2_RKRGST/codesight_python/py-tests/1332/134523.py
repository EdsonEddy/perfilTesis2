n=str(input().lower())
x=len(n)
a=["a","e","i","o","u","y"]
r=""
for i in range (0,x,1):
   m=n[i]
   if m not in a:
        r=r+"."+m
print(r)