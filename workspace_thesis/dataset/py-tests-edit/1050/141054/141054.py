def bina(n):
    binario=''
    while n//2!=0:
        binario=str(n%2)+binario
        n=n//2
    return str(n)+binario

def adec(nb):
    nb=str(nb)
    dec=0
    exp=len(nb)-1
    for i in nb:
        dec+=(int(i)*2**(exp))
        exp=exp-1
    return dec

while True:
    a=int(input())
    b=bina(a)
    d=str(b)[::-1]
    c=adec(d)
    print(c)
