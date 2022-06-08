class Match:
	"""docstring for Match"""
	def __init__(self, sig1, sig2, A, B, threshold):

		self.colors = [[143,231,37],[244,24,181],[76,148,192],[173,180,88],
		[212,160,56],[246,22,70],[120,92,176],[165,215,53],
		[165,121,103],[231,37,143],[24,181,244],[148,192,76],
		[180,88,173],[160,56,212],[22,70,246],[92,176,120],
		[215,53,165],[121,103,165],[231,143,37],[24,244,181],
		[148,76,192],[180,173,88],[160,212,56],[22,246,70],
		[92,120,176],[215,165,53],[121,165,103],[37,143,231],
		[181,244,24],[192,76,148],[88,173,180],[56,212,160],
		[70,246,22],[176,120,92],[53,165,215],[103,165,121]]
		self.Sig1 = sig1
		self.Sig2 = sig2
		self.Tokens1 = A
		self.Tokens2 = B
		self.Threshold = threshold
		self.Code1 = []
		self.Code2 = []
		self.Count = []
		self.Checked = []
		#print(type(sig1),type(sig2),type(A),type(B),)

	def add(self, i, j, k):
		self.Code1.append(i)
		self.Code2.append(j)
		self.Count.append(k)
		self.Checked.append(False)
	
	def getSize(self):
		return len(self.Code1)

	def getData(self):
		val = [[0 for _ in range(3)] for _ in range(len(self.Code1))]
		for i in range(len(self.Code1)):
			val[i][0] = self.Code1[i]
			val[i][1] = self.Code2[i]
			val[i][2] = self.Count[i]
		return val

	def getIntegerData(self):
		val = [[0 for _ in range(3)] for _ in range(self.countChecked())]
		j = 0
		for i in range(len(self.Code1)):
			if self.Checked[i]:
				val[j][0] = self.Code1[i]
				val[j][1] = self.Code2[i]
				val[j][2] = self.Count[i]
				j += 1;
		return val

	def getObjectData(self):
		val = [[0 for _ in range(5)] for _ in range(len(self.countChecked()))]
		j = 0
		for i in range(len(self.Code1)):
			if self.Checked[i]:
				val[j][0] = j + 1
				val[j][1] = self.Code1[i]
				val[j][2] = self.Coun2[i]
				val[j][3] = self.Count[i]
				val[j][4] = ""
				j += 1;
		return val
	def countChecked(self):
		total = 0
		for i in range(len(self.Code1)):
			if self.Checked[i]:
				total += 1
		return total
	def getTokenData(self, select):
		data = None
		if select == 1:
			data = [[0 for _ in range(5)] for _ in range(len(self.Tokens1))]
			for i in range(len(self.Tokens1)):
				data[i][0] = i
				data[i][1] = self.Tokens1[i].getToken()
				data[i][2] = self.Tokens1[i].getWord()
				data[i][3] = self.Tokens1[i].getLine()
				data[i][4] = self.Tokens1[i].getMark()
		elif select == 2:
			data = [[0 for _ in range(5)] for _ in range(len(self.Tokens2))]
			for i in range(len(self.Tokens2)):
				data[i][0] = i
				data[i][1] = self.Tokens2[i].getToken()
				data[i][2] = self.Tokens2[i].getWord()
				data[i][3] = self.Tokens2[i].getLine()
				data[i][4] = self.Tokens2[i].getMark()
		return data

	def switchPosition(self, i, j):
		a = self.Code1[i]
		b = self.Code2[i]
		c = self.Count[i]
		self.Code1[i] = self.Code1[j]
		self.Code2[i] = self.Code2[j]
		self.Count[i] = self.Count[j]
		self.Code1[j] = a
		self.Code2[j] = b
		self.Count[j] = c
	def Sort(self, type):
		for i in range(len(self.Count)):
			for j in range(i + 1, len(self.Count)):
				if type == 1:
					if self.Code1[j] > self.Code1[i]:
						self.switchPosition(i,j)
				elif type == 2:
					if self.Code2[j] > self.Code2[i]:
						self.switchPosition(i,j)
				elif type == 3:
					if self.Count[j] > self.Count[i]:
						self.switchPosition(i,j)

	def mark(self):
		for i in range(self.getSize()):
			a = self.Code1[i]
			b = self.Code2[i]
			count = self.Count[i]
			ini = 0
			while (ini < count) and not self.Tokens1[a + ini].getMark() and not self.Tokens2[b + ini].getMark():
				ini += 1
			if ini == count:
				for j in range(count):
					self.Tokens1[a + j].mark()
					self.Tokens2[b + j].mark()
				self.Checked[i] = True

	def getTokensLength(self, id):
		tokens = 0
		if id == 1:
			tokens = len(self.Tokens1)
		elif id == 2:
			tokens = len(self.Tokens2)
		return tokens
	def getSignature(self, num):
		sig = None
		if num == 1:
			sig = self.Sig1
		elif id == 2:
			sig = self.Sig2
		return sig