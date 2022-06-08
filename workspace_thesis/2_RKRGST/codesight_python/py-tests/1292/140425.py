from sys import stdin, stdout
 
for n in stdin:
    n = int(n)
    if(n == 0):
        break
    cad = stdin.readline()
    v = cad.split(" ")
    res = 0
    for i in range(n):
        v[i] = int(v[i])
        res+=v[i]
    stdout.write(str(res) + '\n')