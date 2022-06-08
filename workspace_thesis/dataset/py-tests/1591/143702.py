m = "2,3,5,7"
s = int(input())
for y in range(s):
    n = input()
    r = ""
    for x in n:
        if x in m:
            r +=x
    if r == "":
        print(-1)
    else:
        print(r)