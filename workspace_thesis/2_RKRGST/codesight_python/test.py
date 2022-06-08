from Codesight import Codesight

path1 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\dataset\\py-tests\\1003\\137797.py"
path2 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\dataset\\py-tests\\1003\\145676.py"

files = [path1, path2]

percentages = [10,25,50,75,90]
for threshold in percentages:
	program = Codesight(files)
	precision = program.compareAll(threshold)[0][1]
	print("threshold=", threshold, "precision=", precision)