def palindromo(s):
    est= str(s)
    if est==est[::-1]:
        return True
    else:
        return False
while True:
    n= int(input())
    c=0
    for i in range (n):
        s=int(input())
        if palindromo(s):
            c=c+1
    print(c)