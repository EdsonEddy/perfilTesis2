from sys import stdin
for hg in stdin:
    n=int(hg)
    l=input().split()
    j=0


    for i in l:
        if int(i)>int(j):
            max=int(i)
        j=max
    j=10000000000*999999
    for h in l:
        if int(h)<int(j):
            min=int(h)
        j=min

    if hg!=1:

        jl=max-min

        print(jl)
    else:


        print('0')