c=str(input())
a=[]
for k in c:
	if k not in a:
		a.append(k)
a.sort()
l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(len(l)):
	if l[i] not in a:
		print(l[i])
		break
else:
    print(-1)