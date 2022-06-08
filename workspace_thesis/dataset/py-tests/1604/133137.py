import sys

if __name__ == '__main__':
    for i in sys.stdin:
        i = i.split()
        print(int(i[0], int(i[1])))
