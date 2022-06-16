import keyword
from .Token import Token

class Signature:
	def __init__(self, file):
		self.totalLines = None
		self.dataTypes =["str", "unicode", "list", "tuple", "set", "frozenset", "dict", "int", "long", "float", "bool"]
		self.Punctuation = [" ","\t",".",",","<",">","/","?",";",
							":","\'","\"","~","[","]","{","}","\\","|","!","@","#","$","%","^","&","*",
							"(",")","-","+","=","^"]
		
		"""
		self.ReservedWords = ["asm","auto","bool","break","case",
							"catch","char","class","const","continue","default","delete","do","double",
							"else","enum","extern","float","for","friend","goto","if","inline","int",
							"long","namespace","new","operator","private","protected","public",
							"register","return","short","signed","sizeof","static","struct","switch",
							"template","this","throw","try","typedef","union","unsigned","using",
							"virtual","void","volatile","while"]
		"""
		self.ReservedWords = keyword.kwlist + self.dataTypes
		self.file = file
		self.LexicalStream = ""
		lineCounter = 0
		i = 0
		self.Tokens = []
		try:
			reader = open(self.file, "r")
			line = None
			lineTokens = []
			words = None
			for line in reader:
				lineCounter += 1
				line = self.trimComments(line.strip())
				words = self.separateWords(line.strip())
				if words != None:
					lineTokens = self.getLexicalStream(words).split(" ")
					for i in range(len(words)):
						self.Tokens.append(Token(lineTokens[i], words[i], lineCounter))
						self.LexicalStream += " " + lineTokens[i]
			reader.close()
		except Exception as e:
			print(type(e))
		self.totalLines = lineCounter
		self.LexicalStream = self.LexicalStream.strip()

	def trimComments(self, line):
		if len(line) > 0 and line[0:1] == "#":
			line = ""
		return line
	def toString(self, vector):
		cad = ""
		for i in vector:
			cad = cad + " " + str(i)
		return cad.strip()
	def copy(self):
		return Signature(self.file)
	def getFile(self):
		return self.file
	def getFileName(self):
		return self.file
	def getTotalLines(self):
		return int(self.totalLines)
	def getNumTokens(self):
		return len(self.Tokens)
	def getLexicalStream(self):
		return self.LexicalStream
	def getLexicalStream(self, word):
		stream = ""
		token = ""
		for i in word:
			token = i
			if self.isReservedWord(token):
				stream += " LITERAL_" + token
			else:
				if self.isPunctuation(token):
					if token == "(": stream += " LPAREN"
					if token == ")": stream += " RPAREN"
					if token == "{": stream += " LCURLY"
					if token == "}": stream += " RCURLY"
					if token == "[": stream += " LBRACK"
					if token == "]": stream += " RBRACK"
					if token == "=": stream += " ASSIGN"
					if token == "<": stream += " LT"
					if token == ">": stream += " BT"
					if token == "+": stream += " PLUS"
					if token == "-": stream += " MINUS"
					if token == "*": stream += " TIMES"
					if token == "/": stream += " DIV"
					if token == "?": stream += " QUEST"
					if token == "!": stream += " ADMIR"
					if token == ",": stream += " COMMA"
					if token == ".": stream += " DOT"
					if token == ";": stream += " SEMI"
					if token == ":": stream += " TWODOT"
					if token == "@": stream += " AT"
					if token == "#": stream += " SHARP"
					if token == "%": stream += " PERCENT"
					if token == "\"": stream += " QUOTE"
					if token == "&": stream += " AMPERS"
					if token == "$": stream += " DOLLAR"
					if token == "\\": stream += " BCKSLSH"
					if token == "\'": stream += " SQUOTE"
					if token == "~": stream += " TILDE"
					if token == "^": stream += " CARET"
					if token == "|": stream += " VERBAR"
				else:
					if self.isInt(token):
						stream += " NUM_INT"
					elif self.isFloat(token):
						stream += " NUM_FLOAT"
					else:
						stream += " IDENT"
		return stream.strip()
	def getWords(self):
		words = []
		for i in self.Tokens:
			words.append(i.getWord())
		return words
	def getTokens(self):
		tokens = []
		for i in self.Tokens:
			tokens.append(i.getToken())
		return tokens
	def getMarks(self):
		marks = []
		for i in self.Tokens:
			marks.append(i.getMark())
		return marks

	def getTokenData(self):
		tokens = []
		for i in self.Tokens:
			tokens.append(i.copy())
		return tokens

	def isDataType(self, word):
		return word in dataTypes

	def isDouble(self, word):
		try:
			word = float(word)
			return True
		except Exception as e:
			return False
	def isInt(self, word):
		try:
			word = int(word)
			return True
		except Exception as e:
			return False
	def isFloat(self, word):
		try:
			word = float(word)
			return True
		except Exception as e:
			return False
	def isLong(self, word):
		try:
			word = int(word)
			return True
		except Exception as e:
			return False
	def isPunctuation(self, letter):
		return letter in self.Punctuation
	def isReservedWord(self, word):
		return word in self.ReservedWords
	def mark(self, index):
		self.Tokens[index].mark()
	def unmark(self, index):
		self.Tokens[index].unmark()
	def separateWords(self, line):
		words = None
		if line != None and not line.strip() == "":
			words = []
			i = 0
			while i < len(line):
				if self.isPunctuation(line[i : i + 1]):
					if i == 0:
						words.append(line[i : i + 1].strip())
					else:
						words.append(line[0 : i])
						if not line[i : i + 1].strip() == "":
							words.append(line[i: i + 1])
					line = line[i + 1: len(line)].strip()
					i = 0
				else:
					i += 1
			if i == len(line) and not line.strip() == "":
				words.append(line)
		return words