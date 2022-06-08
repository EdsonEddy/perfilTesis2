import collections
while True:
    try:
        cad=str(input())
        l=collections.Counter(cad)
        la=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        for i in la:
            if i in l:
                print(i+"="+str(l[i]))
        print()
    except ValueError:
        break