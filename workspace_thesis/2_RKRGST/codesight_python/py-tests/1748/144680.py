import itertools
cad= list(map(str,input().split()))
cad=cad[0]
for i in itertools.permutations(cad):
    for j in range(len(i)):
        print(i[j], end=(""))
    print("")
