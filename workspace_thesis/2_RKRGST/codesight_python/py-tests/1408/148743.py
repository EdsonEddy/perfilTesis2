n=int(input())
s=input()
no=["Alvaro","Edwin","Gabriel"]
s=[i for i in s]
a=["A","B","C"]*n
a1=0
e=["B","A","B","C"]*n
e1=0
g=["C","C","A","A","B","B"]*n
gz=0
for k in range(n):
    if s[k]==a[k]:
        a1=a1+1
    if s[k]==e[k]:
        e1=e1+1
    if s[k]==g[k]:
        gz=gz+1
l=[a1,e1,gz]
y=max(l)
print(y)
for u in range(3):
    if l[u]==y:
        print(no[u])