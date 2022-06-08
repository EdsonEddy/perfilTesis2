while True:
    x = input()
    if len(x)==1:
        if 'a'<= x <='z':
            print('minuscula')
        elif 'A'<= x <='Z':
            print('mayuscula')
        x = x.lower()
        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
            print('vocal')
        else:
            print('consonante')