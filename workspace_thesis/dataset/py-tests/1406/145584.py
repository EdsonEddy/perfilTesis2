while True:
    try:
        x=int(input())
        l1=[int(e) for e in input().split()]
        l2=[int(e) for e in input().split()]
        p=(sum(l1)+sum(l2))/x
        lp=[]
        c=0
        for j in range(x):
            lp.append(l1[j]+l2[j])
        for z in lp:
            if z<p:
                c+=1
        print(c)
    except ValueError:
        break
    
