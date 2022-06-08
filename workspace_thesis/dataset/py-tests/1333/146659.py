def f(l):
    t=[]
    for i in range(len(l)):
        z=l[i:len(l)]
        t.append(z)
    t.sort()
    for y in range(len(t)):
        print(t[y])
l=input()
f(l)