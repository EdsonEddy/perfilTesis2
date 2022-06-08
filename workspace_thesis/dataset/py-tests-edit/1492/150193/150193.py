t, c = input(), input()
idx = -1
while True:
	idx = t.find(c, idx+1)
	if idx > 1:
		print(idx)
	else:
		break