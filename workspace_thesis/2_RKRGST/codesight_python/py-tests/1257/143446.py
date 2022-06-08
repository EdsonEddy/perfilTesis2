r = int(input())
for i in range(r):
    t1 = input()
    t2 = input()
    t1 = t1.replace(' ','')
    t2 = t2.replace(' ','')
    t1 = sorted(t1)
    t2 = sorted(t2)
    if t1 == t2:
        print("Si")
    else:
        print("No")
    print(end="")