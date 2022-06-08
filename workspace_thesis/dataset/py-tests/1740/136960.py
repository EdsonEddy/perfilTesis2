while True:
    n = int(input())
    if n > 0 :
        cx = n
        c = 1
        for i in range(1,n+1):
            print(('-'*cx)+str(i)*c+('-'*cx))
            print()
            cx-=1
            c+=2