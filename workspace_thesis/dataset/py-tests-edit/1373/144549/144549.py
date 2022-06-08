may='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
min='abcdefghijklmnopqrstuvwxyz'
vocales='aeiou'
vocmay='AEIOU'
n=str(input())
if n in may:
    print('mayuscula')
elif n in min:
    print('minuscula')
if n in vocales or n in vocmay:
    print('vocal')
else:
    print('consonante')