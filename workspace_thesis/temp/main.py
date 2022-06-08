def levenshtein(X, Y):
	m = len(X) + 1
	n = len(Y) + 1
	t = [[0 for _ in range(n)] for _ in range(m)]
	for i in range(1, m):
		t[i][0] = i
	for i in range(1, n):
		t[0][i] = i
	for i in range(1, m):
		for j in range(1, n):
			cost = 0
			if not X[i - 1] == Y[j - 1]:
				cost = 1
			t[i][j] = min(t[i - 1][j - 1] + cost, t[i][j - 1] + 1, t[i - 1][j] + 1)
	return t

A = "ACAATCC"
B = "AGCATGC"

for _ in levenshtein(A, B):
	print(_)
