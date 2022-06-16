from .lexer import Lexer
from .sequence_alignment import Sequence_alignment

class Sced_algorithm:
	def __init__(self, file_name_a, file_name_b, D):
		self.file_name_a = file_name_a
		self.file_name_b = file_name_b
		self.D = D
	
	def get_per_similarity(self):
		lexer_a = Lexer(self.file_name_a)
		lexer_b = Lexer(self.file_name_b)
		tokens_a = lexer_a.tokens
		tokens_b = lexer_b.tokens
		algorithm = Sequence_alignment(tokens_a, tokens_b, self.D)
		edit_dis = algorithm.levenshtein_min_space_time()
		max_len = max(len(tokens_a), len(tokens_b))
		percentage = (1 - edit_dis / max_len) * 100
		return percentage