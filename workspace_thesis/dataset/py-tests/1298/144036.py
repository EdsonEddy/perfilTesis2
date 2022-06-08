while(True):
    array=input().split()
    c=""
    for i in range(len(array)-1,0,-1):
        if i!=1:
            c=c+array[i]+" "
        else:
            c=c+array[i]
    print (c)