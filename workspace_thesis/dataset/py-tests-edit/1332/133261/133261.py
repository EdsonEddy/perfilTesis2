cadena=str(input())
x=cadena.lower()
s=""
dat=["a","e","i","o","u","y"]
for i in x:
    if i in dat:
        s=s+''
    else:
        s=s+'.'+i
print(s)
