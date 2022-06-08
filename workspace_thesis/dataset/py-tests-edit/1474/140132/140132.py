z=[]
x=int(input())
a=input()
b=input()
a1=a.split(" ")
b1=b.split(" ")
for i in range(x):
    a1[i]=int(a1[i])
    b1[i]=int(b1[i])
for i in range(x):
    s=input()
    if s=='+':
        t=a1[i]+b1[i]
        z.append(t)
    else:
        if s=='*':
            t=a1[i]*b1[i]
            z.append(t)
        else:
            if s=='>':
                if a1[i]>b1[i]:
                    z.append(a1[i])
                else:
                    z.append(b1[i])
            else:
                if s=='<':
                   if a1[i]<b1[i]:
                      z.append(a1[i])
                   else:
                      z.append(b1[i])
for i in range(x):
    print(z[i])