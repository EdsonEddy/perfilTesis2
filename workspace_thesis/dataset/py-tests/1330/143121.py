s,r = input().split()
r = int(r)
s1 = ""
ns = s
for i in range(1,r+1):
    cs = len(s)
    if cs > 1:
        temp = len(s)
        ultimo = s[cs - 1]
        s1 = ultimo + s1
        s = s[:temp -1]
        ns = s1 + s
print(ns)