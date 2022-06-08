while(EOFError):
    n = input()
    for i in range (int(n)):
        num = input()
        sum = 0
        for i in range (int(num)):
            sum+=int(input())
        print(sum)