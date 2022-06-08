while True:
    try:
        x=int(input())
        if x==0:
            break
        l=[str(e) for e in input().split()]
        print("".join(sorted(l,reverse=True)))
    except ValueError:
        break