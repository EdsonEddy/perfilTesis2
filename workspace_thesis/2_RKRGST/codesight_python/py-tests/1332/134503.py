a = input()
a = a.lower()
m = "a"
n = "e"
o = "i"
p = "o"
q = "u"
r = "y"
h = "."
i = ""
for x in a:
    if(x == m or x == n or x == o or x == p or x == q or x == r):
        continue
    else:
        i = i + h + x
print(str(i))
