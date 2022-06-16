class Token:
	
	def __init__(self, token, word, line):
		self.Token = token
		self.Word = word
		self.Line = line
		self.Mark = False

	def getData(self):
		return [self.Token, self.Word, self.Line, self.Mark];
		
	def getLine(self):
		return self.Line

	def getMark(self):
		return self.Mark

	def getToken(self):
		return self.Token

	def getWord(self):
		return self.Word

	def mark(self):
		self.Mark = True

	def unmark(self):
		self.Mark = False

	def copy(self):
		copy = Token(self.Token, self.Word, self.Line)
		if self.Mark:
		    copy.mark()
		return copy