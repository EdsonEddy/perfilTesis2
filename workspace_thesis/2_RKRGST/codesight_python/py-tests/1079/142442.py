lv=['a','e','i','o','u']
lc=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
def vocal1(x):
	lx=list(x)
	for i in range(len(x)):
		if lx[i] in lv:
			vo1='true'
			break
		else:
			vo1='false'
	return vo1
def cons3(y):
	ly=list(y)
	if len(y)>=3:
		i=0
		while i< len(y)-2:
			if  (ly[i] in lv)and (ly[i+1]in lv)and (ly[i+2]in lv):
				cons='true'
				break
			elif (ly[i] in lc)and (ly[i+1]in lc)and (ly[i+2]in lc):
				cons='true'
				break
			else:
				cons='false'
			i+=1
	else:
		cons='false'
	return cons
def ocurr(z):
	lz=list(z)
	if len(z)>1:
		for k in range(len(z)-1):
			if (lz[k]==lz[k+1]) and ( lz[k] == 'e' or lz[k] =='o'):
				ocur='false'
			elif (lz[k]==lz[k+1]) :
				ocur='true'
				break
			else:
				ocur='false'
	else:
		ocur='false'
	return ocur
n=input()
while n != 'end':
	if vocal1(n)=='true' and cons3(n)=='false' and ocurr(n)=='false':
		print('<'+n+'>'+' is acceptable.')
	else:
		print('<'+n+'>'+' is not acceptable.')
	n=input()