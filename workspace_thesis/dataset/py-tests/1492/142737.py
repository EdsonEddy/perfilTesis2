a=input()
c=input()
j=0
for i in (a):
    if i==c:
        b=a[j: ].find(c)+j
        j=j+b+1
        print(b)