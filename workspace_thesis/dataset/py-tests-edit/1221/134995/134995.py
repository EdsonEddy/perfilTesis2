a, b, c = map(int, input().split())
if a>b and a>c:
	m1 = a
	if b>c:
		m2 = b
		m3 = c
	else:
		m2 = c
		m3 = b
else:
	if b>c and b>a:
		m1 = b
		if c>a:
			m2 = c
			m3 = a
		else:
			m2 = a
			m3 = c
	else:
		m1 = c
		if b>a:
			m2 = b
			m3 = a
		else:
			m2 = a
			m3 = b
print(str(m3) + ' ' + str(m2) + ' ' + str(m1))