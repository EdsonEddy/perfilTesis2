a=input()
l=["a","e","i","o","u","y"]
b=a.lower()
s=""
for i in range (len(a)):
   c=b[i]
   if c in l:
       s=s+""
   else:
       s=s+"."+c
print(s)