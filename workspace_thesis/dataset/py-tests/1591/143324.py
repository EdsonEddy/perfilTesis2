t = int(input())
while t:
    t -=1
    s = input()
    n = len(s)
    sw = 1
    for i in range(n):
        if s[i]=='2' or  s[i]=='3' or s[i]=='5' or  s[i]=='7':
            print(s[i],end='')
            sw = 0
    if sw: print('-1')
    else:print()