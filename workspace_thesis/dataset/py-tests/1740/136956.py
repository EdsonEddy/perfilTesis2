while True:
    n = int(input())
    cx = n
    c = 1
    for i in range(1,n+1):
        print(('-'*cx)+str(i)*c+('-'*cx))
        cx-=1
        c+=2