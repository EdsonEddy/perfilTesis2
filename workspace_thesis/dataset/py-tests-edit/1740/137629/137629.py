
def series_dobles(_n):
    c=0
    for i in range(_n):
        c+=1
        for j in  range(_n+_n+1):
            if j<_n-c+1 or j>_n+c-1:
                print("-",end="")
            else:
                print(c,end="")
        print(end="\n")
n=int(input())
series_dobles(n)