while True:
    x=input()
    i=0
    sw=0
    while i<len(x)-1:
        if x[i]!="r" and x[i]!="l" and x[i]==x[i+1]:
            sw=1
        i=i+1
    if sw==1:
        print("si")
    else:
        print("no")
    
