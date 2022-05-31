from collections import deque

def bfs():
	global n_left, n_right, adjacency_list, match, distance, k
	distance = [-1 for _ in range(n_left + n_right)]
	q = deque()
	k = 1e9
	for u in range(n_left):
		if match[u] == -1:
			distance[u] = 0
			q.append(u)
	while len(q) > 0:
		u = q.popleft()
		if distance[u] > k:
			break
		for v in adjacency_list[u]:
			if distance[v] == -1:
				distance[v] = distance[u] + 1
				if match[v] == -1:
					k = distance[v]
				else:
					distance[match[v]] = distance[v] + 1
					q.append(match[v])
	return k != 1e9

def dfs(u):
	global adjacency_list, distance, match, visited, k
	for v in adjacency_list[u]:
		if not visited[v] and distance[v] == distance[u] + 1:
			visited[v] = True
			if match[v] != -1 and distance[v] == k:
				continue
			if match[v] == -1 or dfs(match[v]):
				match[v] = u
				match[u] = v
				return True
	return False

def hopcroft_karp(G):
	global n_left, n_right, adjacency_list, match, visited
	n_left = G.n_left
	n_right = G.n_right
	adjacency_list = G.adjacency_list
	match = [-1 for _ in range(n_left + n_right)]
	mcbm = 0
	while bfs():
		visited = [0 for _ in range(n_left + n_right)]
		for u in range(n_left):
			if match[u] == -1:
				if dfs(u):
					mcbm += 1
	return mcbm