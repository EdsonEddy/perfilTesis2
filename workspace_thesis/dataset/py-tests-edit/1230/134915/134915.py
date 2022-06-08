ts = int(input())
sf = ts // 60
seg = ts % 60
h = sf // 60
min = sf % 60
print(h, min, seg)