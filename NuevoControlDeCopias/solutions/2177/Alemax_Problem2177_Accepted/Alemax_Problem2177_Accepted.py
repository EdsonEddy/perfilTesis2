def sumard(n):
    if len(str(n)) == 1:
        return str(n)
    else:
        return sumard(
            str(n).count("1") + str(n).count("2") * 2 + str(n).count("3") * 3 + str(n).count("4") * 4 + str(n).count(
                "5") * 5 + str(n).count("6") * 6 + str(n).count("7") * 7 + str(n).count("8") * 8 + str(n).count(
                "9") * 9)
for i in range(int(input())):
    a, b = map(int, input().split())
    a = str(a)[::-1]
    sum = ""
    for i in range(len(a) + 1 - b):
        sum = sum + sumard(int(a[i:i + b]))
    print(sum[::-1])
