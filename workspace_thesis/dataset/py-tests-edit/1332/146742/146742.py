def elim(x):
    vocales = ['a','A','e','E','i','I','o','O','u','U','Y','y']
    mayus=["A","B","C","a","b","c"]
    punt="."
    res = ''

    for letra in x:
        if letra not in vocales:
            res=res+punt+letra
    return res
n=input().lower()
print(elim(n))