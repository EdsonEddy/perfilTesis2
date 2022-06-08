n = int(input())
a = b = 0
for i in range(n):
   c = int(input())
   if c&1:a += 1
   else:  b += 1
if a > b:print('Gana el jugador 1!')
else: print('Gana el jugador 2!')
