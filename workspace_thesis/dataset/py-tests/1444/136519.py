con=int(input())
for x in range (0,con):
    n = int(input())
    d = str(bin(n))
    d = d[2:len(d)]
    e = d.count("11")
    print(e)