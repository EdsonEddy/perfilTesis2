num = int(input())

while num>0:
    #n = ['305' ,'14' ,'948' ,'990' ,'777 ','777' ,'63 ','744' ]
    nop = int(input())
    n = input().split()
    m = sorted((n))
    le = []
    for i in n:

        i = int(i)
        le.append(i)
    pr = sorted(le)
    print(*pr)
    num -= 1