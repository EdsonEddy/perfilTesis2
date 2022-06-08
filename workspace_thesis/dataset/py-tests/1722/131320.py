n = int(input())
c = 0
for i in range(n):
    if int(input()) == 2:
        c += 1
if c > n - c:
    print('Gana el jugador 2!')
elif n - c > c:
    print('Gana el jugador 1!')