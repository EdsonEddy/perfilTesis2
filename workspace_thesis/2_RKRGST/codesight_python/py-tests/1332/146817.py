def eli(n):
    l="aeiouy"
    j=""
    i=0
    while i<len(n):
        if n[i]not in l:
            j=j+'.'+n[i]
        i=i+1
    print(j)

n=input().lower()
eli(n)
