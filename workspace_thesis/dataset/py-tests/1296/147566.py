n=int(input())
l=[]
for i in range(n):
    a=input()
    b=a[::-1]
    l.insert(0,b)
n=0
for y in range(len(l)):
    n=l[y]
    print(n)