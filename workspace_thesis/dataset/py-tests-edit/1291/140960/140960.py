import sys

def main(elems):
    i = 0
    for x in elems:
        i += x
    print(i)

if __name__ == '__main__':
    for line in sys.stdin:
        elems = [int(x) for x in line.split()]
        main(elems)