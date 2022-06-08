casos = int(input())
for i in range(casos):
    x, y = map(int, input().split())
    if 2 <= x <= 40 and 2 <= y <= 40:
        l = [1]*y
        a = -1 * y
        while x - y >= 0:
            l.append(sum(l[a::]))
            x -= 1
        print(l[len(l)-1])