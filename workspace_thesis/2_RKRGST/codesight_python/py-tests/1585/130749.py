
import sys

if __name__ == '__main__':
    for line in sys.stdin:
        n = int(line)
        i = input().split()
        j = input().split()
        X, Y = [], []
        for x in i:
            X.append(int(x))
        for y in j:
            Y.append(int(y))

        X.sort()
        Y.sort()
        rx = 0
        for i in X:
            if i > 0:
                if i >= n:
                    break
                else:
                    rx += 1
        ry = 0
        for i in Y:
            if i > 0:
                if i >= n:
                    break
                else:
                    ry += 1

        print((rx + 1) * (ry + 1))
