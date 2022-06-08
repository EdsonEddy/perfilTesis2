n = input()
sa = 0
st = 0
c = 0
for j in n:
    st = st + int(j)
for i in range((len(n))-1):
    sa = sa + int(n[i])
    if (sa % 3) == 0 and ((st - sa) % 3) == 0:
        c = c + 1

print(c)
