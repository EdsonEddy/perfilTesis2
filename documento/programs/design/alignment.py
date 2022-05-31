def get_lcs(X, Y):
	m = len(X) + 1
	n = len(Y) + 1
	c = [[0 for _ in range(n)] for _ in range(m)]
	for i in range(1, m):
		for j in range(1, n):
			if X[i - 1] == Y[j - 1]:
				c[i][j] = c[i - 1][j - 1] + 1
			elif c[i - 1][j] >= c[i][j - 1]:
				c[i][j] = c[i - 1][j]
			else:
				c[i][j] = c[i][j - 1]
	lcs_cost = c[m - 1][n - 1]
	max_len = max(len(X), len(Y))
	return (lcs_cost / max_len)