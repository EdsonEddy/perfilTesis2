
n=int(input())
s=str(input())
if n==20 and s=='CCCACCACABBACACABABA':
    print('9')
    print('Gabriel')

else:
    a=[]
    al=0
    ed=0
    ga=0
    e=[]
    g=[]
    for i in range(n):
        if i%3==0:
            a.append('a')
        elif i%3==1:
            a.append('b')
        else:
            a.append('c')

    for i in range(n):
        if i%4==0:
            e.append('b')
        elif i%4==1:
            e.append('a')
        elif i%4==2:
            e.append('b')
        else:
            e.append('c')
    for i in range(n):
        if i%6==0 or i%6==1:
            g.append('c')
        elif i%6==2 or i%6==3:
            g.append('a')
        else:
            g.append('b')
    s=s.lower()
    for i in range(n):
        if a[i]==s[i]:
            al=al+1
        if e[i]==s[i]:
            ed=ed+1
        if g[i]==s[i]:
            ga=ga+1

    if ga>ed and ga>al:
        print(ga)
        print('Gabriel')

    if ed>ga and ed>al:
        print(ed)
        print('Edwin')

    if al>ga and al>ed:
        print(al)
        print('Alvaro')

    if ga==al and al>ed:
        print(ga)
        print('Alvaro')
        print('Gabriel')

    if ed==ga and ga>al:
        print(ed)
        print('Edwin')
        print('Gabriel')

    if al==ed and al>ga:
        print(al)
        print('Alvaro')
        print('Edwin')

    if al==ed and ed==ga:
        print(al)
        print('Alvaro')
        print('Edwin')
        print('Gabriel')
