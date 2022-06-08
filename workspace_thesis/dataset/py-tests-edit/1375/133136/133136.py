def buscadorDeCadena(prueb):
    pruebA = prueb.lower()
    pruebB = pruebA.find("oro")
    if "oro" in pruebA:
        pruebc = pruebB + 2
        print(pruebB, pruebc)
    else:
        print(pruebB)
prueb = input()
buscadorDeCadena(prueb)