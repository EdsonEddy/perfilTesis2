ss=1
while ss==1:
    n = input().split()
    if len(n) > 0:
        ta = len(n) - 1
        sw=1
        lista=[]
        c=0
        sal=''
        for i in n:
            if sw==0:
                lista.insert(c,i)
                c=c+1
            else:
                sw=0
        c=c-1
        for j in range(ta):
            if j==ta-1:
                sal = sal + (lista[c])
                c = c - 1
            else:
                sal=sal+(lista[c])+' '
                c=c-1
        print(sal)
    else:
        ss = 0
