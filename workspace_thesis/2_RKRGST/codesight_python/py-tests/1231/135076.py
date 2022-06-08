cont = True
while cont:
	a, b, c = map(int, input().split())
	if a<24 and b<60 and c<60:
		cont = False

c = c + 1

if c==60:
	b = b + 1
	c = 0

if b==60:
	a = a + 1
	b = 0

if a<10:
	a = str(0)+str(a)
if b<10:
	b = str(0)+str(b)
if c<10:
	c = str(0)+str(c)

if a == 24:
	a = str(0)+str(0)
	b = str(0)+str(0)
	c = str(0)+str(0)

print(str(a)+':'+str(b)+':'+str(c))