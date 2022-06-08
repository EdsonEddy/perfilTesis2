import sys

if __name__ == '__main__':
    for cadena in sys.stdin:
        cadena = cadena.rstrip()
        b = cadena[::-1]
        c1 = ''
        c2 = ''
        sw = False
        for i in range(len(b) // 2 +1):
            c1 += cadena[i]
            c2 = b[i] + c2
            if c1 == c2:
                sw = True
                break
        if sw:
            print('si')
        else:
            print('no')
