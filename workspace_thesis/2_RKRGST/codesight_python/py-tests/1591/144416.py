from math import log10
def primo(num):
    k=2
    if num==1 or num==0:
        sw=0
    else:
        while num%k!=0 and k<=num//2:
            k=k+1
        if k>num//2:
            sw=1
        else:
            sw=0
    return sw
n=int(input())
for i in range(n):
    x=int(input())
    cd=int(log10(x))
    nn=0
    while x!=0:
        d=x//10**cd
        x=x%10**cd
        cd=cd-1
        s=primo(d)
        if s==1:
            nn=(nn*10)+d
    if nn!=0:
        print(nn)
    else:
        print('-1')
