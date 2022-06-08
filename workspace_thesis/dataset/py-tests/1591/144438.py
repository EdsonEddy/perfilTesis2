import math

def primo(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True

casos = int(input())
for i in range(casos):
    number = input()
    nn = ''
    for j in number:
        aux = int(j)
        if primo(aux):
            nn += j
    if len(nn)> 0 :
        print(nn)
    else:
        print(-1)