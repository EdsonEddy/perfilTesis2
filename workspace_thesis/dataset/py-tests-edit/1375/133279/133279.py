palabra = str(input())
palabra = palabra.lower()
a = palabra.find("oro")
if (a == -1):
    print ("-1")
else:
    print (a, a+2)