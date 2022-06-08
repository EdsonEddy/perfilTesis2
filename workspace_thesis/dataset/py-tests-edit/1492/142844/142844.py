n=input()
x=len(n)
while x >100:
    n=input()
    x = len(n)
y=input()
c=-1
for i in n:
    c=c+1
    if i == y:
        print(c)
