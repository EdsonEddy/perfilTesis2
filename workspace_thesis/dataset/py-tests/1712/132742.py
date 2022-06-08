s = 0
while True:
    n = input()
    if n == "fin":
        break
    
    for i in range(int(n)):
        a = int(input())
        s = s+ a
    print(s)
    s = 0
