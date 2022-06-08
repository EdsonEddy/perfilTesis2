p = int(input())
for _ in range(p):
    c, pa = map(int, input().split())
    cu = c // 3
    pal = pa // 2
    mat = (c + pa)
    if cu > pal:
        picotas = pal
    else:
        picotas = cu 

    if picotas != 0:
      ct = picotas * 3
      pat = picotas * 2
      tmat = ct + pat
      r = mat - tmat
    else:
      r = mat
    print(picotas,r)