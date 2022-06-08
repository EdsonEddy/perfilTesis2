from Match import Match
from Signature import Signature
class Codesight:
	def __init__(self, files):
		self.Files = files
		self.Signatures = []
		for i in files:
			self.Signatures.append(Signature(i))

	def getSourceCode(self, index):
		sourcecode = ""
		try:
			reader = open(self.Signatures[index].file, "r")
			i = 0
			for line in reader:
				i += 1
				sourcecode += str(i) + "   " + str(line) + "\n"
			reader.close()
		except Exception as e:
			sourcecode = str(e)
		return sourcecode
	def getFileName(self, index):
		return self.Files[index]
	def getFilesName(self):
		names = []
		for i in self.Files:
			names.append(i)
		return names
	def getSignature(self, index):
		sig = None
		if type(index) == int:
			if index < len(self.Signatures):
				sig = self.Signatures[index].copy()
		elif type(index) == str:
			for i in self.Signatures:
				if index == i.getFileName():
					sig = i.copy()
		return sig
	def greedyStringTiling(self, sig1, sig2, threshold):
		if type(sig1) == int and type(sig2) == int and type(threshold) == int:
			return self.greedyStringTiling(self.Signatures[sig1], self.Signatures[sig2], threshold)
		A = sig1.getTokenData()
		B = sig2.getTokenData()
		matches = Match(sig1, sig2, A, B, threshold)
		maxmatch = threshold
		for a in range(sig1.getNumTokens()):
			for b in range(sig2.getNumTokens()):
				j = 0
				while ((a + j) < sig1.getNumTokens()) and ((b + j) < sig2.getNumTokens()) and (A[a + j].getToken() == B[b + j].getToken()) and not A[a + j].getMark() and not B[b + j].getMark():
					j += 1
				if j > 0 and j >= maxmatch:
					matches.add(a,b,j)
		if matches.getSize() > 0:
			matches.Sort(3)
			matches.mark()
		return matches
	def getPercentMatch(self, match):
		percent = 1
		coverage = 0
		total = 0
		copiedSequences = match.countChecked()
		data = match.getIntegerData()
		for i in range(copiedSequences):
		    coverage += data[i][2]
		total = match.getTokensLength(1) + match.getTokensLength(2)
		percent = (2 * coverage) / total
		return percent * 100
		#return percent
	def compareAll(self, Threshold):
		result = None
		i = 0
		j = 0
		table = [[0 for _ in range(len(self.Signatures))] for _ in range(len(self.Signatures))]
		for i in range(len(self.Signatures)):
			for j in range(i, len(self.Signatures)):
				if i == j:
					table[i][j] = -1
				else:
					result = self.greedyStringTiling(i, j, Threshold)
					result = self.getPercentMatch(result)
					table[i][j] = round(result, 2)
					table[j][i] = round(result, 2)
		return table
	def getTitles(self):
		titles = []
		for i in self.Signatures:
			titles.append(str(i))
		return titles
	def getNumSignatures(self):
		return len(self.Signatures)