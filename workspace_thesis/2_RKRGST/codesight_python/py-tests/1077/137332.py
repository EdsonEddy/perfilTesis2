x = 1
c = 1
while c != 0:
    a = int(input())
    if a == 0:
        c = 0
    else:
        lista = ''
        aux = a
        while a != 0:
            d =  a % 10
            # print(d)
            # print(x,'x')
            if x == 1:
                if d == 0:
                    lista = ('') + lista
                elif d == 1:
                    lista = ('i') + lista
                elif d == 2:
                    lista = ('ii') + lista
                elif d == 3:
                    lista = ('iii') + lista
                elif d == 4:
                    lista = ('iv') + lista
                elif d == 5:
                    lista = ('v') + lista
                elif d == 6:
                    lista = ('vi') + lista
                elif d == 7:
                    lista = ('vii') + lista
                elif d == 8:
                    lista = ('viii') + lista
                elif d == 9:
                    lista = ('ix') + lista
            if x == 2:
                if  d == 0:
                    lista = ('') + lista
                elif d == 1:
                    lista = ('x') + lista
                elif d == 2:
                    lista = ('xx') + lista
                elif d == 3:
                    lista = ('xxx') + lista
                elif d == 4:
                    lista = ('xl') + lista
                elif d == 5:
                    lista = ('l') + lista
                elif d == 6:
                    lista = ('lx') + lista
                elif d == 7:
                    lista = ('lxx') + lista
                elif d == 8:
                    lista = ('lxxx') + lista
                elif d == 9:
                    lista = ('xc') + lista
            if x == 3:
                if  d == 0:
                    lista = ('') + lista
                elif d == 1:
                    lista = ('c') + lista
                elif d == 2:
                    lista = ('cc') + lista
                elif d == 3:
                    lista = ('ccc') + lista
                elif d == 4:
                    lista = ('cd') + lista
                elif d == 5:
                    lista = ('d') + lista
                elif d == 6:
                    lista = ('dc') + lista
                elif d == 7:
                    lista = ('dcc') + lista
                elif d == 8:
                    lista = ('dccc') + lista
                elif d == 9:
                    lista = ('cm') + lista
            if x == 4:
                if  d == 0:
                    lista = ('') + lista
                elif d == 1:
                    lista = ('m') + lista
                elif d == 2:
                    lista = ('mm') + lista
                elif d == 3:
                    lista = ('mmm') + lista
            x += 1
            a = int(a/10)
        x = 1
        print(str(aux)+' => '+lista)