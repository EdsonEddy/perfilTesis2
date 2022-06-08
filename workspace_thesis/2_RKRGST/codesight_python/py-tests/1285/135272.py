from sys import stdin
for n in stdin:
    n = int(n)
    s1 = 0
    s2 = 0
    cd = 0
    while(n > 0):
        if(cd % 2 == 0):
            s1 = s1 + (n % 10)
        else:
            s2 = s2 + (n % 10)
        n//=10
        cd+=1
    if(s1 == s2):
        print("SI")
    else:
        print("NO")
