from sys import stdin, stdout
 
for n in stdin:
    n = int(n)
    cad = stdin.readline()
    s = cad.split(" \n")
    v = str(s[0]).split(" ")
    v = list(map(int, v))
    v.sort()
    v.append(int(-1))
    for i in range(n):
        if(v[i] != (i + 1)):
            stdout.write(str(i + 1) + '\n')
            break
