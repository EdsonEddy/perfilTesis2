def f(x):
	s ='0123456789'
	c = 0
	for i in s:
		if(i==x):
			return c
		c += 1
	return -1
y = input()
c = s = 0
for i in y:
	c += f(i)
	if(c%3==0):
		s += 1
#print(s)
i = len(y) - 1
m = c = 0
while(i>=0):
	c += f(y[i])
	if(c%3==0):
		m += 1
	i -= 1
#print(m)
if(m==s):print(m-1)
else:print(0)
