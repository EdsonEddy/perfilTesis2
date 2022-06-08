import sys

for n in sys.stdin:
    n =int(n)
    s=input()
    v=s.split(" ")
    cd=0
    for i in range (len(v)):
        if(v[i]==v[n-1]):
            cd+=1
    print (cd)
