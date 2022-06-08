y = int(input())
s1 = 0
s2 = 0
for _ in range(y):
    i = int(input())
    if i == 2:
        s2 = s2 + 1
    if i == 1:
        s1 = s1 + 1

if s1 < s2:
    print("Gana el jugador 2!")
else:
    print("Gana el jugador 1!")
