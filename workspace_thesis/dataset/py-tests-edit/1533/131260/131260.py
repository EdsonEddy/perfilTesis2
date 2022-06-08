from sys import stdin, stdout
for n in stdin:
    a,b = map(int, n.split())
    mid = a//2
    if(a % 2 != 0):
        mid+=1
    if(b <= mid):
        stdout.write(str(2*(b-1) + 1)+"\n")
    else:
        b-=mid
        stdout.write(str(2*b)+"\n")