while True:
    try:
        s=str(input())
        t=sorted(set(list(s)))
        l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for i in range(0,len(l)):
            if l[i] in t:
                sw=1
            else:
                sw=0
                j=(l[i])
                break
        if sw==1:
            print(int(-1))
        else:
            print(j)
    except ValueError:
        break