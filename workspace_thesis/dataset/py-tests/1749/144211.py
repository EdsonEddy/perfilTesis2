import re, string

def remove_punctuation ( frase ):
    return re.sub('[%s]' % re.escape(string.punctuation), ' ', frase)
frase=str(input())
respuesta=remove_punctuation(frase)
print(respuesta)