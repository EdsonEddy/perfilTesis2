while True:
    vec = input().split()
    vec = list(map(int, vec))
    vec.sort()
    s1, s2 = 0, 0
    for i in range(0, len(vec), 2):
        s1 += vec[i]
    for i in range(1, len(vec), 2):
        s2 += vec[i]
    print(abs(s2 - s1))