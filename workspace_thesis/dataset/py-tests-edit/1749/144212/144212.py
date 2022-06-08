def elimina(s):
    signos=".,)(;:"
    s_sin_signos=""
    for letra in s:
        if letra not in signos:
            s_sin_signos =s_sin_signos + letra
        else:
            s_sin_signos = s_sin_signos + " "
    return s_sin_signos
x=input()
print(elimina(x))