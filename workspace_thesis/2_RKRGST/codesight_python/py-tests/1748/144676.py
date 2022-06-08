import itertools
n = list(map(str,input().split()))
n = n[0]
for i in itertools.permutations(n):
    for j in range(len(i)):
        print(i[j],end='')
    print('')