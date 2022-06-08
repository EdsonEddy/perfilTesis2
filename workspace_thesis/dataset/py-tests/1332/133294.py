a=input()
a=a.lower()
c=""
e=""
for b in a:
    if b=="a" or b=="e" or b=="i"or b=="o"or b=="u"or b=="y":
        b=""
    c=c+b
for d in c:
    e=e+"."+d
print(e)