if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    counts = [0]*101
    for e in arr:
        counts[e] += 1

    matching_pairs = 0
    for c in counts:
        if c//2 > 0:
            matching_pairs += c//2

    print(matching_pairs)
