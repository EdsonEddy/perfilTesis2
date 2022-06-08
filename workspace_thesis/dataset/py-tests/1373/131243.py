i=input()
if(i==i.upper()):
        if('A'==i or 'E'==i or 'I'==i or 'O'==i or 'U'==i):
                print('mayuscula'+"\n"+'vocal')
        else:
                print('mayuscula'+"\n"+'consonante')
elif('a'==i or 'e'==i or 'i'==i or 'o'==i or 'u'==i):
        print('minuscula'+"\n"+'vocal')
else:
        print('minuscula'+"\n"+'consonante')