from sys import stdin, stdout
while(True):
    cad,x = map(str,stdin.readline().split('\n'))
    if cad=='#':
        break
    cad = cad.replace('%','%25')
    cad = cad.replace(' ','%20')
    cad = cad.replace('!','%21')
    cad = cad.replace('$','%24')
    cad = cad.replace('(','%28')
    cad = cad.replace(')','%29')
    cad = cad.replace('*','%2a')
    stdout.write(cad+'\n')