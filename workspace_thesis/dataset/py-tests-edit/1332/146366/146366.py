n=input()
dd=n.lower()
vocales=["a","e","i","o","u","y"]
new=[]
for i in dd:
    if i not in vocales:
        new.append(i)
d=".".join(new)
w="."+d
print(w)