s,r=map(str,input().split())
long=len(s)
if(long>=1 and long<=40):
    if(int(r)>=0 and int(r)<=long):
        inver=s[:-int(r)]
        rota=s[-int(r):]
        sol=rota+inver
    print(sol)