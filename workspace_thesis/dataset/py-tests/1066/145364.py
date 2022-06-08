from sys import *
n=int(stdin.readline())
for i in range(n):
	cad=stdin.readline()
	cad=cad[:len(cad)]
	lM,lm,num,car=0,0,0,0
	for j in range(len(cad)):
		cr=ord(cad[j])
		if 65<=cr and cr<=90:
			lM=1
		if 97<=cr and cr<=122:
			lm=1
		if 48<=cr and cr<=57:
			num=1
		if cad[j]=='@' or cad[j]=='.' or cad[j]=='_' or cad[j]=='>' or cad[j]=='<' or cad[j]=='-':
			car=1
	if lM==1 and lm==1 and num==1 and car==1:
		stdout.write(str("Dale no te jackiaran esta vez.\n"))

	else:
		stdout.write(str("No va dar Botas.\n"))
