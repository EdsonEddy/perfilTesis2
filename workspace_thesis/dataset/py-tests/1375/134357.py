oro=[]
cad = input()
c,o,r,co = -1,0,0,0
for i in range(0,len(cad)):
	c=c+1
	if o==0 and (cad[i]== 'o' or cad[i]=='O'):
		o=1
		continue
	if o==1:
		if cad[i]=='r' or cad[i]=='R':
			r=1
			continue
		o=0
	if r==1:
		if cad[i]=='o' or cad[i]=='O':
			co=c-2
			r,c=0,0
			continue
		else:
			co=-1
if co>=0:
	print(co,co+2)
else:
	print('-1')