s = input()
for i in range(97, 122):
	if chr(i)  not in s:
		print(chr(i))
		break
else:
	print(-1)
	