a = 1
c = 0
while(a != 0):
    a = int(input())
    for y in range(a):
        b = input().split()
        l = len(b)
        if(l == a):
            for x in range(len(b)):
                c = int(b[x]) + c
            print(c)
            a = int(input())
            c = 0
            l = 0
        else:
            break
    
