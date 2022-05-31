import pygments.token as token
import pygments.lexers as lexer

class Lexer:
	def __init__(self, file_name):
		self.file_name = file_name
		self.tokens_per_line = []
		self.dict_keywords = {}
		self.clean_tokenize()

	def compute_hash(self, s):
		p = 31
		m = 1e9 + 9
		hash_value = 0
		p_pow = 1
		for c in s:
			hash_value = (hash_value + (ord(c) - 97 + 1) * p_pow) % m
			p_pow = (p_pow * p) % m
		self.dict_keywords[s] = hash_value

	def get_hash(self, s):
		if self.dict_keywords.get(s, None) == None:
			self.compute_hash(s)
		return self.dict_keywords[s]

	def num_convert(self, num):
		try:
			integer = int(num)
			return integer
		except Exception as e:
			try:
				double = float(num)
				return double
			except Exception as e:
				return "N"

	def clean_tokenize(self):
		file = open(self.file_name, "r")
		text_string = file.read()
		file.close()
		lex = lexer.guess_lexer_for_filename(self.file_name, text_string)
		lex_tokens = lex.get_tokens(text_string)
		tokens = []
		for element in lex_tokens:
			token_type = element[0]
			token_value = element[1]
			if "\n" in token_value:
				self.tokens_per_line.append(tokens)
				tokens = []
			elif token_type in token.Text:
				pass
			elif token_type in token.Keyword:
				tokens.append(self.get_hash(token_value))
			elif token_type in token.Name.Function:
				tokens.append("F")
			elif token_type in token.Name:
				tokens.append("V")
			elif token_type in token.Literal.String:
				tokens.append("S")
			elif token_type in token.Literal.Number:
				tokens.append(self.num_convert(token_value))
			elif token_type in token.Operator:
				tokens.append(token_value)
			elif token_type in token.Punctuation:
				tokens.append(token_value)
			elif token_type in token.Comment:
				pass
			else:
				tokens.append("X")