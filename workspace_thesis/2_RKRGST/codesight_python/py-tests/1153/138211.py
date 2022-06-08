import sys

if __name__ == '__main__':
    for linea in sys.stdin:
        linea = linea.rstrip()
        nombre = []
        habilidades = []
        for i in linea:
            try:
                num = int(i)
                habilidades.append(num)
                continue
            except ValueError:
                t = 1 
            
            if i == '+':
                x = habilidades.pop(-1)
                y = habilidades.pop(-1)
                habilidades.append(x+y)
            elif i == '*':
                x = habilidades.pop(-1)
                y = habilidades.pop(-1)
                habilidades.append(x*y)
            else:
                nombre.append(i)
        nombre.reverse()
        print(''.join(nombre)+": habilidad", habilidades.pop(-1))

