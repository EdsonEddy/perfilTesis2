def series_dobles(_n):
    c=1
    j=0
    while c<=_n:
        if j<_n+_n+1:
            if j<_n-c+1 or j>_n+c-1:
                print("-",end="")
            else:
                print(c,end="")
            j+=1
        else:
          print(end="\n")
          j=0
          c+=1

n=int(input())
series_dobles(n)