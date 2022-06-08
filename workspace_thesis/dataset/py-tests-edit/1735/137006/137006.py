while True:
    n = (input())
    ini = 4
    cx = 2
    if n != None:
        n = int(n)
        if n > 0:
            for i in range(n):
                if i == n - 1:
                    print(ini)
                    ini = ini * 3 - cx
                    cx += 2
                else:
                    print(ini, end='  ')
                    ini = ini * 3 - cx
                    cx += 2
        else:
            print('error')
        print()
        print('error')