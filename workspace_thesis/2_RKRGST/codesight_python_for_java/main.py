from Codesight import Codesight
from Signature import Signature
import os

threshold = 30
path1 = "test-cpp"
files = []
for i in os.listdir(path1):
	path2 = path1 + "\\" + i
	files.append(path2)

Program = Codesight(files)
result = Program.compareAll(threshold)

for i in range(len(result)):
	for j in range(len(result)):
		print(round(result[i][j], 2), end="\t")
	print()