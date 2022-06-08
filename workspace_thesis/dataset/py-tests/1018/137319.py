x = int(input())
for k in range(x):
    a, b = map(int,input().split())
    if a > b:
        print('>')
    elif a < b:
        print('<')
    else:
        print('=')