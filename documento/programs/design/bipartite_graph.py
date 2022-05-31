class Bipartite_graph:
	def __init__(self, n_left, n_right):
		self.n_left = n_left
		self.n_right = n_right
		self.num_vertex = n_left + n_right
		self.adjacency_list = [[] for _ in range(self.num_vertex)]
	
	def add_edge(self, u, v):
		self.adjacency_list[u].append(v)
		self.adjacency_list[v].append(u)