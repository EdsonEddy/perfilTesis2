cad=input().lower()
n=""
for i in range (len(cad)):
    if(cad[i]!='a'and cad[i]!='e'and cad[i]!='i'and cad[i]!='o'and cad[i]!='u'and cad[i]!='y'):
        n=n+'.'+cad[i]
print(n)
