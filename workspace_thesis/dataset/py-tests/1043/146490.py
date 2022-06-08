import math

casos = int(input())

for i in range(casos):
    mat = list(map(int, input().rstrip().split()))
    piedras = mat[0]
    palos = mat[1]
    pip = piedras // 3
    r1 = piedras % 3
    pap = palos // 2
    r2 = palos % 2
    pic = min(pip, pap)
    pip = abs(pic - pip)
    r1 += pip*3
    pap = abs(pic - pap)
    r2 += pap*2
    rt = r1 + r2
    print(pic,rt)