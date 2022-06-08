try:
    while (True):
        n = int(input())
        r = 0
        while (n != 0):
            r = r + int(input())
            n = n - 1
        print(r)
except:
    False