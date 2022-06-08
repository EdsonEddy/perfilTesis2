from sys import stdin
for j in stdin:
    l=[1]
    n=int(j)
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            if i not in l:
                l.append(i)
            if n//i not in l:
                l.append(n//i)
    l.sort()
    if n not in l:
        l.append(n)
    print('Divisores de ',end="")
    print(n,end="")
    print(':',end=" ")
    for k in range(len(l)):
        if k!=len(l)-1:
            print(l[k] ,end=" ")
        else:
            print(l[k])