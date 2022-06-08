cadena=str(input())#introdusca una cadena de texto
for k in cadena:
    ñ= (ord(k))
    ñ=str((bin(ñ)))
    win = ñ[:1] + ñ[2:]

    while len(win)<8:
        win='0'+win

    print(win,end="")
print()
