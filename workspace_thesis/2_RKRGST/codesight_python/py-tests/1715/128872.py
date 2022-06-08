import itertools


def subset(elements, n):
    return set(itertools.combinations(elements, n))


while True:
    try:
        suma, n_el = [int(x) for x in input().split()]
        v = [int(x) for x in input().split()]

        cont = 0
        for i in range(len(v)):
            subsets = subset(v, i)
            for perm in subsets:
                if sum(perm) == suma:
                    cont += 1

        print(cont)
    except EOFError:
        break
