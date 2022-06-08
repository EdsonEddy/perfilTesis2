while True:
    a,b = input().split()
    la,lb =[],[]
    c=0
    for i in a:
        la.append(int(i))
    for j in b:
        lb.append(int(j))
    for k in range(len(la)):
        if la[k] != lb[k]:
            c+=1
        else:
            pass
    if c == 1 or c==0:
        print('feliz')
    else:
        print('lentes')