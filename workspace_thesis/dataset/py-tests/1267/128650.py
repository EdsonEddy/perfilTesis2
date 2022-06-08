while EOFError:
    grada=1
    n=int(input())
    if(n>=0 and n<=1000):
        if(n==0):
            print(grada)
        else:
            for i in range(n):
                grada=grada+2
            print(grada)
    else:
        exit()