n=int(input())
l=[]
for n in range(n):
    a=input()
    l.append(a)
for i in range(len(l)-1,-1,-1):
    print(l[i][::-1])