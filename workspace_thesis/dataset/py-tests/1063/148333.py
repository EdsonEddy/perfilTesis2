caso_prueba = int(input())
if 1 <= caso_prueba<= 10:
    for i in range (caso_prueba):
        a, b = map(int, input() .split())
        r = a % b
        print (r)
