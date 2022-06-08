from sys import stdin, stdout
for n in stdin:
    n = int(n)
    if(n == 0):
        break
    cad1=stdin.readline()
    c1=cad1.split(" ")
    c=0
    for i in range(n):
        c=c+int(c1[i])
    print (c)