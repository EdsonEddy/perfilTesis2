casos=int (input ())
for i in range (casos):
    elem=int (input ())
    nros=list(map(int,input().split()))
    nros.sort()
    print (*nros)