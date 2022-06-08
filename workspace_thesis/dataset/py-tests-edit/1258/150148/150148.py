dict = dict()
for _ in range(int(input())):
	n = input()
	try:
		dict[n] += 1
	except:
		dict[n] = 1
for it in sorted(dict):
	if dict[it] > 1:
		print(it, end=' ')
print()