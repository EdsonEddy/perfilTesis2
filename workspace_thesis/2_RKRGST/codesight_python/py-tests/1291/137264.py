import sys
#for line in sys.stdin:
while True:
    s = 0
    for line in map(int, input().split()):
        n = int(line)
        s = s + n
    print(s)
