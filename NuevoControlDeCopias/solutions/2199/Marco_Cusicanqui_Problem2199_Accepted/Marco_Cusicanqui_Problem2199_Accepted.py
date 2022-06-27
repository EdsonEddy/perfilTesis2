import sys

cin=sys.stdin
for line in cin:
    x=int(line)
    for i in range(x): print('   *   ',end='')
    print()
    for i in range(x): print('  /#\\  ',end='')
    print()
    for i in range(x): print(' /###\\ ',end='')
    print()
    for i in range(x): print('___#___',end='')

