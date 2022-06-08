from sys import stdin
for line in stdin:
    e=int(line)
    n=1
    if e==0:
        print(n)
    elif e==-1:
        break
    else:
         for i in range (e):
            n=n+2
         print(n)