def elimina_sig(s):
        signos=".,:;()"
        aux=""
        for letra in s:
            if letra not in signos:
                aux=aux+letra
            else:
                aux=aux+" "

        return aux


x=input()
print(elimina_sig(x))
