import sys
for linea in sys.stdin:
    sumalista=linea.split()
    print(eval('+'.join(sumalista)))

