n=int(input())
a = "   *   "
a1 = a
b = "  /#\  "
b1 = b
c = " /###\ "
c1 = c
d = "___#___"
d1 = d
for x in range(n -1):
    a1 = a1 + a
    b1 = b1 + b
    c1 = c1 + c
    d1 = d1 + d
print(a1)
print(b1)
print(c1)
print(d1)
