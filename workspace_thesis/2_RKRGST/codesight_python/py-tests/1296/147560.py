c=int(input())
l=[]
for i in range(c):
    a=input()
    b=a[::-1]
    l.append(b)
d=l[::-1]
for i in d:
    print(i)