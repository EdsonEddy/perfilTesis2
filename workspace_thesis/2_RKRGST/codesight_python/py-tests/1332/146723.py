import string
frase=input()
vocales="AEIOUYaeiouy"
str=""
for k in frase:
    if k in vocales:
        str+=""
    else:
        a=ord(k)
        if a>=65 and a<=90:
            a=a+32
            k=chr(a)
        str+="."+k
print(str)
        