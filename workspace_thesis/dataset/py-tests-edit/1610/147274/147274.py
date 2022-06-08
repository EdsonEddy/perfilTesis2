f=input()
f=f.split('0')
r=''
w=0
for i in f:
	t=i
	for h in t:
		w=w+int(h)
	r=r+str(w)
	w=0
print(r)