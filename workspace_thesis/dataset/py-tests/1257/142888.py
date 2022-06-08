t = int(input())
for i in range(t):
    a = input()
    b = input()
    x = [a[x] for x in range(len(a)) if(a[x] != ' ')]
    y = [b[x] for x in range(len(b)) if(b[x] != ' ')]
    x.sort()
    y.sort()
    if(x == y):
        print("Si")
    else:
        print("No")
    
    
