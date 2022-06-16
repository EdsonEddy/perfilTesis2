import sys

for entrada in sys.stdin:
    n=int(entrada.strip())
    for i in range (1,n+1):
        print('   *   ',end='')
    print('')

    for i in range(1,n+1):
        print('  /#\  ',end='')
    print('')

    for i in range(1,n+1):
        print(' /###\ ',end='')
    print('')

    for i in range(1,n+1):
        print('___#___',end='')
    print('')
