import sys

def criba_eratostenes(n): 
    multiplos = set()
    primos = []
    for i in range(2, n+1): 
        if i not in multiplos: 
            #print(i, end=" ") 
            primos.append(i)
            multiplos.update(range(i*i, n+1, i)) 
    return primos      


def sdig(n):
    if n//10 == 0:
        return n
    else:
        return sdig(n//10) + n%10
      

criba = (criba_eratostenes(1000000))
if __name__ == '__main__':
    for i in sys.stdin:
        inic, fin = i.split()
        for z in range(int(inic), int(fin) + 1):
            if sdig(criba[z]) == sdig(z):
                print(z, criba[z])