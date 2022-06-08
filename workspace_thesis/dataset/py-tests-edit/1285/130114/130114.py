from sys import stdin
for i in stdin:
    n=int(i)
    n=str(n)
    s1=0
    s2=0
    for j in range(len(n)//2):
        c=n[j*2+1]
        s1=s1+int(c)
    k=len(n)
    if k%2==0:
        k=len(n)//2
    else:
        k=len(n)//2+1
    for k in range(k):
        l=n[k*2]
        s2=s2+int(l)
    if s1==s2:
        print('SI')
    else:
        print('NO')