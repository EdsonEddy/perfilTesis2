def nore(nl):
    nl = list()
    for x in a:
        if x in a:
            if x not in nl:
                nl.append(x)
        else:
            return -1
    return nl
while True:
    n = int(input())
    a = list(input().split())
    if n == len(a):
        #a =[10,20,20,10,10,30,50,10,20]
        d = nore(a)
        res = 0
        for x in d:
            f = a.count(x)
            if f/2>=1:
              t = f//2
              res +=t
        print(res)