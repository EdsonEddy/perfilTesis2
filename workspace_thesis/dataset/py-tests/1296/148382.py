n=int(input())
l=[]
for j in range(n):
    n=input()
    l.append(n)
for j in range(len(l)-1,-1,-1):
    l2=l[j]
    for k in range(len(l2)-1,-1,-1):
        print(l2[k][::-1],end='')
    print()