from lexer import Lexer
from alignment import get_lcs
from matching import hopcroft_karp
from bipartite_graph import Bipartite_graph

class Scam_algorithm:
	def __init__(self, file_name_a, file_name_b, tolerance):
		self.file_name_a = file_name_a
		self.file_name_b = file_name_b
		self.tolerance = tolerance / 100
		self.build_graph()

	def build_graph(self):
		lexer_a = Lexer(self.file_name_a)
		lexer_b = Lexer(self.file_name_b)
		tokens_a = lexer_a.tokens_per_line
		tokens_b = lexer_b.tokens_per_line
		n_left = len(lexer_a.tokens_per_line)
		n_right = len(lexer_b.tokens_per_line)
		self.graph = Bipartite_graph(n_left, n_right)
		self.nodes_left = set()
		self.nodes_right = set()
		for idu, u in enumerate(tokens_a):
			for idv, v in enumerate(tokens_b):
				if len(u) == 0 or len(v) == 0:
					continue
				distance = get_lcs(u, v)
				if distance >= self.tolerance:
					self.graph.add_edge(idu - 1, n_left + idv - 1)
					self.nodes_left.add(idu - 1)
					self.nodes_right.add(n_left + idv - 1)
	
	def calculate_dice_index(self):
		mcbm = hopcroft_karp(self.graph)
		left = len(self.nodes_left)
		right = len(self.nodes_right)
		try:
			dice_index = (2 * mcbm) / (left + right)
		except Exception as e:
			dice_index = 0
		return dice_index