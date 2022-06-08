list=["null","Feliz","Triste","Triste","Triste","Triste","Feliz","Feliz","Triste","Triste"]
n=int(input())
for i in range(n):
    z = input()
    while int(z) > 9:
        s = 0
        for i in z:
            s = s + (int(i) ** 2)
        z = str(s)
    print(list[int(z)])
