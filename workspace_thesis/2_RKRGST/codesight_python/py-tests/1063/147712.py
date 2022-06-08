x = int(input())
for i in range(x):
    m, b = map(int, input().split())
    if m>b or True:
        print(m%b)