import math
a,b,c=map(int, input().split())
ca=cb=cc=1
if a>0:
	ca=int(math.log10(a))+1
if b>0:	
	cb=int(math.log10(b))+1
if c>0:
	cc=int(math.log10(c))+1
d=a*10**(cb+cc)+b*10**(cc)+c
e=a*10**(cb+cc)+c*10**(cb)+b
f=b*10**(ca+cc)+a*10**(cc)+c
g=b*10**(ca+cc)+c*10**(ca)+a
h=c*10**(cb+ca)+a*10**(cb)+b
i=c*10**(cb+ca)+b*10**(ca)+a
print(max(d,e,f,g,h,i))
