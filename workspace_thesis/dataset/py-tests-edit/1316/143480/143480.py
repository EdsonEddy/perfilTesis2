from sys import stdin
for n in stdin:
    n = int(n)
    # Lectura
    cad1 = input()
    cad2 = input() 
    v1 = cad1.split(" ")
    v2 = cad2.split(" ")
    v1 = list(map(int, v1))
    v2 = list(map(int, v2))
    #ordenando vectores
    v1.sort()
    v2.sort()
    #ordenando descendente
    v2.reverse()
    res = 0
    for i in range(n):
        res = res + v1[i]*v2[i]
    print(res)