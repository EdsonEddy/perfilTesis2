from sys import *
q=stdin.readline()
q=int(q)
for i in range(q):
    n=stdin.readline()
    n=int(n)
    ans=0
    sw=1
    while  n!=0:
        if n<4 and n!=0:
            sw=0
            break
        if (n&1)==1 and n>=9:
            n-=9
            ans+=1
        if n%4==2 and n>=6:
            n-=6
            ans+=1
        else:
            ans+=n//4
            n%=4
    if sw==1:
        stdout.write(str(ans)+"\n")
    else:
        stdout.write(str(-1)+'\n')