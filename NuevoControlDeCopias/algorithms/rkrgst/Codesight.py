from .Match import Match
from .Signature import Signature

class Codesight:
	def __init__(self, fileA, fileB, Threshold):
		self.SignatureA = Signature(fileA)
		self.SignatureB = Signature(fileB)
		self.Threshold = Threshold

	def greedyStringTiling(self):
		A = self.SignatureA.getTokenData()
		B = self.SignatureB.getTokenData()
		matches = Match(self.SignatureA, self.SignatureB, A, B, self.Threshold)
		maxmatch = self.Threshold
		for a in range(self.SignatureA.getNumTokens()):
			for b in range(self.SignatureB.getNumTokens()):
				j = 0
				while ((a + j) < self.SignatureA.getNumTokens()) and ((b + j) < self.SignatureB.getNumTokens()) and (A[a + j].getToken() == B[b + j].getToken()) and not A[a + j].getMark() and not B[b + j].getMark():
					j += 1
				if j > 0 and j >= maxmatch:
					matches.add(a,b,j)
		if matches.getSize() > 0:
			matches.Sort(3)
			matches.mark()
		return matches

	def get_per_similarity(self):
		match = self.greedyStringTiling()
		percent = 1
		coverage = 0
		total = 0
		copiedSequences = match.countChecked()
		data = match.getIntegerData()
		for i in range(copiedSequences):
		    coverage += data[i][2]
		total = match.getTokensLength(1) + match.getTokensLength(2)
		percent = (2 * coverage) / total
		percentage = round(percent * 100, 2)
		return percentage