l=input()
vocales="aeiouy"
s=""
l=l.lower()
l=list(l)
for i in range(len(l)):
    if l[i] not in vocales:
        s=s+"."+l[i]
print(s)