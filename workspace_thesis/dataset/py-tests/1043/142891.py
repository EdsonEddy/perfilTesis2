n= int(input())
for i in range(n):
    r,p=map(int,input().split())
    contr=r//3
    contp=p//2
    while ( contr != contp ):
         if contr < contp:
           contp = contr
         else:
           contr = contp
    a = r - (3 * contr )
    b = p - (2 * contp )
    print (contr , a+b)