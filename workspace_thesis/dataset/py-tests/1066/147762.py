from sys import * 
def minuscula(c,l):
    for i in range(l):
        b = ord(c[i])
        if b >= 97 and b <= 122 :
            return True
    return False


def mayus(c,l):
    for i in range(l):
        b = ord(c[i])
        if  b >= 65 and b <= 90:
            return True
    return False
    
    
    
def caracte(c,l):
    for i in range(l):
        b = c[i]
        e = ord(c[i])
        if b == '@' or b == '.' or b == '_' or b == '<' or b == '>' or b == '-':
            return True
    return False

def num(c,l):
    for i in range(l):
        b = ord(c[i])
        if b >= 48 and b <= 57:
            return True
    return False
n = int(input())
for i in range(n):
    c = c = stdin.readline().split("\n")
    c = c[0]
       
    l = len(c)
    if minuscula(c,l) and caracte(c,l) and num(c,l) and mayus(c,l):
        print("Dale no te jackiaran esta vez.")
    else:
        print("No va dar Botas.")