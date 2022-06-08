def levenshtein(X, Y):
	m = len(X) + 1
	n = len(Y) + 1
	t = [[0 for _ in range(n)] for _ in range(m)]
	for i in range(0, m):
		t[i][0] = i
	for i in range(1, n):
		t[0][i] = i
	for i in range(1, m):
		for j in range(1, n):
			cost = 0
			if not X[i - 1] == Y[j - 1]:
				cost = 1
			t[i][j] = min(t[i - 1][j - 1] + cost, t[i][j - 1] + 1, t[i - 1][j] + 1)
	return t[m - 1][n - 1]

def levenshtein_min_space(X, Y):
	if len(Y) > len(X):
		X, Y = Y, X
	m = len(X) + 1
	n = len(Y) + 1
	t = [[i for i in range(n)] for _ in range(2)]
	for i in range(1, m):
		t[0], t[1] = t[1], t[0]
		t[0][0] = i - 1
		t[1][0] = i 
		for j in range(1, n):
			cost = 0
			if not X[i - 1] == Y[j - 1]:
				cost = 1
			t[1][j] = min(t[0][j - 1] + cost, t[1][j - 1] + 1, t[0][j] + 1)
	return t[1][n - 1]

def levenshtein_min_time(X, Y, D):
	m = len(X) + 1
	n = len(Y) + 1
	mx = max(len(X), len(Y))
	t = [[mx for _ in range(n)] for _ in range(m)]
	d = ceil(len(Y) * (D / 100))
	for i in range(0, m):
		t[i][0] = i
	for i in range(1, n):
		t[0][i] = i
	for i in range(1, m):
		left = max(1, i - d)
		right = min(n, i + d + 1)
		for j in range(left, right):
			cost = 0
			if not X[i - 1] == Y[j - 1]:
				cost = 1
			t[i][j] = min(t[i - 1][j - 1] + cost, t[i][j - 1] + 1, t[i - 1][j] + 1)	
	return t[m - 1][n - 1]

from math import ceil
def levenshtein_min_space_time(X, Y, D):
	if len(Y) > len(X):
		X, Y = Y, X
	m = len(X) + 1
	n = len(Y) + 1
	d = ceil(len(Y) * (D / 100))
	t = [[_ for _ in range(n)] for _ in range(2)]
	for i in range(1, m):
		t[0], t[1] = t[1], t[0]
		t[0][0] = i - 1
		t[1][0] = i
		left = max(1, i - d)
		right = min(n, i + d + 1)
		for j in range(left, right):
			cost = 0
			if not X[i - 1] == Y[j - 1]:
				cost = 1
			t[1][j] = min(t[0][j - 1] + cost, t[1][j - 1] + 1, t[0][j] + 1)
	return t[1][n - 1]