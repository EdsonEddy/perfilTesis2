while True:
    n=int(input())
    yu=(bin(n))
    yu=yu[2:]
    yu=yu[::-1]
    print(int(yu,2))