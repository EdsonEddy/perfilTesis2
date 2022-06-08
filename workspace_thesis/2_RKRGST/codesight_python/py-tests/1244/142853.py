a = int(input())
m = 1
for x in range(1, a + 1):
    for line in map(str, input().split()):
        if(line == 'rectangle'):
            y = line
        elif(line == 'circle'):
            y = line
        else:
            m = m * float(line)
    if(y == 'circle'):
        m = m ** 2 * 3.14159265359
        print("{0:.2f}".format(m))
    else:
        print("{0:.2f}".format(m))
    m = 1