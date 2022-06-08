n = "y"
while(n != "fin"):
    n = input()
    if(n != "fin"):
        sum = 0
        for i in range (int(n)):
            sum+=int(input())
        print(sum)