def digito(n):
    r=0
    for d in n:
        r=r+pow(int(d),2)
    return r
def happy(n):
    if n==4:
        return False
    u=digito(list(str(n)))
    if u==1:
        return True
    else:
        return happy(u)
c=int(input())
for i in range (c):
    g=int(input())
    if happy(g)==True:
        print("Feliz")
    else:
        print("Triste")