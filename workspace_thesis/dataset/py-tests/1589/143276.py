palabra = "abcdefghijklmnopqrstuvwxyz"
pal = str(input())
for letra in palabra:
    a =(pal.find(letra))
    if (a == -1):
        print(letra)
        break
if (a != -1):
    print("-1")