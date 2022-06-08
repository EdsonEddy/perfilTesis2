cad = input("")
cad = cad.lower()
index=-1
for i in range(len(cad)-2):
	if(cad[i]=='o' and cad[i+1]=='r' and cad[i+2]=='o'):
		index=i
		break
if(index != -1):
	print(index,index+2)
else:
	print(-1)