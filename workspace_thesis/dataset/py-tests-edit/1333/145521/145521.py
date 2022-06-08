a=input()
l=[]*len(a)
for i in range(len(a)):
    b=a[i:]
    l.append(b)
    l.sort()
for j in l:
    print(j)
