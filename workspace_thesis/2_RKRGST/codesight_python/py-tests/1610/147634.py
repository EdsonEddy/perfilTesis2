a=input()
l=[]*len(a)
s=""
h=0
for i in range(len(a)):
    l.append(a[i])
for j in range(len(l)):
    if l[j]=="0" or j==len(l)-1:
        b=l[h:j+1].count("1")
        s=s+str(b)
        h=j
print(s)

