a=input()
b="abcdefghijklmnopqrstvuwxyz"
X=0
for d in b:
    if d not in a:
        X=1
        print(d)
        break
if X==0:
    print("-1")