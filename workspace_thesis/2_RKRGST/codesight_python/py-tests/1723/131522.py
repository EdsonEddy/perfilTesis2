from sys import stdin
for line in stdin:
    k, t = line.split()
    if int(k) <= 999999 and int(t) <= 999999 and len(k) == len(t):
        c = 0
        for i in range(len(k)):
            if k[i] != t[i]:
                c += 1
            if c > 1:
                print('lentes')
                break
        else:
            print('feliz')