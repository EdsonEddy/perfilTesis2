# 1527: Examen arbitrario
# Jhonny
n = int(input())
for i in range(n):
    x = int(input())
    while x > 0:
        dd = x % 100
        if dd == 96:
            print("APLAZADO!")
            break
        x = x // 10
    else:
        print("TE SALVAS :D")