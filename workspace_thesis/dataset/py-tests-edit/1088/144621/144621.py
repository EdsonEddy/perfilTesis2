n = int(input())
for i in range(n):
    cad1 = input()
    cad2 = input()
    v = [0 for i in range(260)]
    mov = 0
    for j in range(len(cad1)):
        v[ord(cad1[j])] = j
    for j in range(1,len(cad2)):
        val = abs(v[ord(cad2[j-1])] - v[ord(cad2[j])])
        mov = mov + val
    print(mov)
