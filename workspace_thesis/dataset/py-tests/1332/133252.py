a=str(input())
x=a.lower()
s=""
v=["a","e","i","o","u","y"]
for y in x:
    if y in v:
        s=s+""
    else:
        s=s+"."+y
print(s)