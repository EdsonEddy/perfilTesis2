try:
    while True:
        n = int(input())
        r = [0, 0, 0]
        while n != 0:
            s = input()
            v = s.split()
            r[0] = r[0] + int(v[0])
            r[1] = r[1] + int(v[1])
            r[2] = r[2] + int(v[2])
            n = n - 1

        if r == [0, 0, 0]:
            print("YES")
        else:
            print("NO")
except:
    False