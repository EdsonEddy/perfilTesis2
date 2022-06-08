import itertools
while True:
    v=str(input().strip())
    re=[]
    for i in itertools.permutations(v):
        r=""
        for g in i:
            r+=g
        print(r)