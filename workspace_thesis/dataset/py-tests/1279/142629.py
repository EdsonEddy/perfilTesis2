def returnP(x):
     l='abcdefghijklmnopqrstuvwxyz'
     for j in range (0,len(l)):
         if x == l[j]:
             break
     return int(j)
while True:
    try:
        k,cad=map(str,input().split())
        if int(k) > 0 and 1<=len(cad)<=50:
            imp=''
            k=int(k)
            k=k%26
            for i in range (0,len(cad)):
                l = 'abcdefghijklmnopqrstuvwxyz'
                if cad[i]=='_':
                    let=' '
                    imp=imp+let
                elif cad[i] not in l:
                    let=cad[i]
                    imp=imp+let
                else:
                    let=l[((k+returnP(cad[i]))%26)]
                    imp=imp+let
            print(imp.upper())
    except ValueError:
        break