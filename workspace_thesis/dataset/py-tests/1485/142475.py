import sys
for mod in sys.stdin:
    mod = int(mod)
    modu = 0
    for x in range(mod):
        nn = 0
        a = int(input())
        b = a
        while(a != 0):
            dig = a % 10
            a = a // 10
            nn = nn * 10 + dig
        if(b == nn):
            modu = modu + 1
    print(modu)