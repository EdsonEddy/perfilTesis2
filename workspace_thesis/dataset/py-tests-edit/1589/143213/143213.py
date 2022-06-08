x=str(input())
v=[97,98,99,100,101,102,103,104,105,106,
   107,108,109,110,111,112,113,114,115,
    116,117,118,119,120,121,122]
for i in range(len(x)):
	c=int(ord(x[i:i+1]))
	if len(v)!=0 and c in v:
		ind=v.index(c)
		v.pop(ind)
if len(v)!=0:
	print(chr(v[0]))
else:
	print("-1")