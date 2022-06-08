from sys import *#stdin stdout
for n in stdin:
    n=int(n)
    v=list(range(n+1))
    may=0
    cad=stdin.readline().split()
    for i in range(len(cad)):
        v[int(cad[i])]=-1
    for i in range(1,n+1):
        if v[i]==i:
            stdout.write(str(i)+'\n')