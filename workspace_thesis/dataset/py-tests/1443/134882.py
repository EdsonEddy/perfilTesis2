while True:
    a=int(input())
    sf = 0
    foo = 0
    p = []
    for j in range(1, a):
        if a % j == 0:
            foo = foo + j
    for k in range(1, a):
        if a % k == 0:
            p.append(k)
    for l in p:
        sf = sf + l
    if foo == a:
        print('Perfecto')
    elif sf < a:
        print('Deficiente')
    else:
        print('Abundante')