while True:
    x = input()
    m = len(x)//2
    mi = m
    md = m
    
    while mi >0:
        if x[:mi] == x[md:]:
            print("si")
            break
        else:
            mi -=1
            md +=1
    if mi <= 0:
        print("no")
