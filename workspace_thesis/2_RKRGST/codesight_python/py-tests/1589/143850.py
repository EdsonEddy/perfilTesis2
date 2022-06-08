l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z']
c=input()
s=c
ls=list(s)
ls.sort()
if len(ls)>=len(l):
	for i in l:
		if i not in ls:
			r=1
			break
		else:
			r=0
	if r ==1:
		for w in l:
			if w not in ls:
				print(w)
				break
	else:
		print(-1)
else:
	for w in l:
		if w not in ls:
			print(w)
			break