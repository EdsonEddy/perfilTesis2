xx, yy, zz = [int(x) for x in input().split()]
if zz > 58:
	zz = 0
	yy += 1
else:
	zz += 1
if yy > 59:
	yy = 0
	xx += 1
if xx > 23:
	xx = 0
print("%02d:%02d:%02d" %(xx, yy, zz))