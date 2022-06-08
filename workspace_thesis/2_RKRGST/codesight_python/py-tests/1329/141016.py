def main():
    n, a, b = input().split()# 
    n, a, b = int(n),int(a),int(b)
    
    v = [int(x) for x in input().split()]
    
    Quicksort(v, a, b)

    salida = ""
    for i in v:
        salida += str(i) + " "
    print(salida.rstrip())

def Quicksort(v, a, b):
    matris = [0]*len(v)    
    buf = 0
    frm = a
    to = b
    pivote = v[(frm+to)//2]
    while True:
        while v[frm] < pivote:
            frm += 1
        while v[to] > pivote:
            to -= 1
        if frm <= to:
            buf = v[frm]
            v[frm] = v[to]
            v[to] = buf
            frm += 1
            to -= 1
        if frm > to:
            break
    if a < to:
        Quicksort(v, a, to)
    if frm < b:
        Quicksort(v, frm, b)
    matris = v

if __name__ == '__main__':
    main()