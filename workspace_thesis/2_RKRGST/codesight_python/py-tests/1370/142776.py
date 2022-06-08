s = ''
while True:  
    n = input()
    if (str(n) == str(s)):
        break
    else:
        n = int(n)
        i = 1
        e = 2
        while (e <= n):
            e = e * 2
            i = i + 1
        print (i)