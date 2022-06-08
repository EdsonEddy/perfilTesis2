vocales = 'aeiouy'
cadena = input().lower()
conv = ''
for i in cadena:    
    if i not in vocales:
        conv += '.'+i
print(conv)