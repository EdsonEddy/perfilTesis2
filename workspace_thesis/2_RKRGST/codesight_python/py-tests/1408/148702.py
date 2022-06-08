def alvaro(t):
    a= []
    l = ['A', 'B', 'C']
    for i in range(t):
        a.append(l[i%3])
    return a

def edwin(t):
    a = []
    sw = 1
    for i in range(t):

        if i %2==0:
            a.append("B")
        else:
            if sw == 1:
                a.append("A")
                x = 1
                sw = sw + x
            elif sw == 2:
                a.append("C")
                x = 1
                sw = sw - x
    return a


def gabriel(t):
    c = 0
    cx = 0
    l = 0
    le = ["C","A","B"]
    a =[]
    for i in range(t):
        if cx == 0 and c <= 2:
            a.append(le[0])
            c += 1
            if c == 2:
                cx += 1
                c = 0
                continue
        if cx == 1 and c <= 2:
            a.append(le[1])
            c += 1
            if c == 2:
                cx += 1
                c = 0
                continue
        if cx == 2 and c <= 2:
            a.append(le[2])
            c += 1
            if c == 2:
                cx = 0
                c = 0
                continue
    return a



x = int(input())
y = input()
z = list("".join(y))
a = alvaro(x)
e = edwin(x)
g = gabriel(x)
ca = 0
ce = 0
cg = 0
for i in range(x):
    if a[i] == y[i]:
        ca += 1
    if e[i] == y[i]:
        ce += 1
    if g[i] == y[i]:
        cg += 1
aux = max(ca,ce,cg)
print(aux)
if ca == aux:
    print("Alvaro")
if ce == aux:
    print("Edwin")
if cg == aux:
    print("Gabriel")