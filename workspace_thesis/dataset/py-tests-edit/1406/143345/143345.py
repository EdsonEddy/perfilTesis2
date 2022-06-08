from sys import stdin
for x in stdin:
    n = int(x)
    habVerbal = [int(a) for a in input().split()]
    habNum = [int(b) for b in input().split()]
    lp = []
    sp = 0
    er = 0
    for i in range(n):
        p = habVerbal[i] + habNum[i]
        sp = sp + p
        lp.append(p)
    for i in range(n):
        if lp[i] < sp/n:
            er = er + 1
    print(er)