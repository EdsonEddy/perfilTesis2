import sys
from os import listdir
from os.path import isfile, join
from timeit import default_timer
from sced_algorithm import Sced_algorithm

path_source = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\dataset\\py-tests\\"
start_time = default_timer()
if len(sys.argv) > 1:
	D = 100
	if len(sys.argv) == 3:
		D = int(sys.argv[1])
		path1 = sys.argv[2]
	else:
		path1 = sys.argv[1]
	mypath = path_source + path1
	save_path = path1
	try:
		onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
		n = len(onlyfiles)
		precision = [[0 for _ in range(n)] for _ in range(n)]
		for i in range(n):
			for j in range(i, n):
				if i == j:
					precision[i][i] = 100
				else:
					a = mypath+"\\"+onlyfiles[i]
					b = mypath+"\\"+onlyfiles[j]
					program = Sced_algorithm(a, b, D)
					precision[i][j] = program.get_per_similarity()
					precision[j][i] = precision[i][j]
		path_out1 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\" + save_path + "_SCED_D_" + str(D) + "_PRECISION.csv"
		import numpy as np
		x1 = np.asarray(precision)
		np.savetxt(path_out1, x1, delimiter=',')
	except Exception as e:
		print(str(e))
else:
	print("params error:")
elapsed_time = default_timer() - start_time

path_out2 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\execution_time.txt"
with open(path_out2, "a") as myfile:
    myfile.write("\n" + save_path + " SCED elapsed_time=" + str(elapsed_time))

"""
Commands
python main.py 1115

default score = 0
python main.py 5 1115

"""