import sys

if __name__ == "__main__":
    for line in sys.stdin:
        vectores = []
        for i in range(0, int(line)):
            vectores.append(input().split())
        x = 0
        y = 0
        z = 0
        for vec in vectores:
            x += int(vec[0])
            y += int(vec[1])
            z += int(vec[2])
        if x == 0 and y == 0 and z == 0:
            print("YES")
        else:
            print("NO")