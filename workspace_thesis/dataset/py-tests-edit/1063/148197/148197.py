x = int(input())
while(x != 0):
    a, b = map(int, input().split())
    s = a % b
    print(s)
    x = x - 1
