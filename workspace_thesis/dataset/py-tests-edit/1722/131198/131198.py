n = int(input())
sum1 = 0
sum2 = 0
for x in range(n):
    jug = int(input())
    if jug == 1:
        sum1 = sum1+1
    if jug == 2:
        sum2 = sum2+1
if sum1 > sum2:
    print('Gana el jugador 1!')
else:
    print('Gana el jugador 2!')