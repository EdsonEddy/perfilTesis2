while True:
    try:
        n = int(input())
        l1 = [int(e) for e in input().split()]
        l2 = [int(i) for i in input().split()]
        o = sum(l1)
        lt = len(l2)
        l2 = sorted(l2, reverse=True)
        while True:
            o = o - l2[0]
            if o <= 0:
                l2.remove(l2[0])
                break
            else:
                l2.remove(l2[0])
        print(lt - len(l2))
    except ValueError:
        break