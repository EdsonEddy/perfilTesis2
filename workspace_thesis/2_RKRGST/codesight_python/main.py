import sys, os
from Codesight import Codesight
from Signature import Signature
from timeit import default_timer

if len(sys.argv) > 1:
	start_time = default_timer()
	threshold = 30
	if len(sys.argv) == 3:
		threshold = int(sys.argv[1])
		path1 = sys.argv[2]
	else:
		path1 = sys.argv[1]
	path_source = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\dataset\\py-tests\\"
	path1 = path_source + path1
	files = []
	for i in os.listdir(path1):
		path2 = path1 + "\\" + i
		files.append(path2)
	path1 = path1.split("\\")
	path_out1 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\" + path1[-1] + "_RKRGST_" + "T_" +str(threshold) + "_PRECISION.csv"
	#path_out2 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\" + path1[-1] + "_RKRGST_" + "T_" +str(threshold) + "_TIME.csv"
	Program = Codesight(files)
	precision = Program.compareAll(threshold)

	import numpy as np
	x1 = np.asarray(precision)
	np.savetxt(path_out1, x1, delimiter=',')
	
	elapsed_time = default_timer() - start_time
	path_out2 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\execution_time.txt"
	with open(path_out2, "a") as myfile:
		myfile.write("\n" + path1[-1] + " RKRGST" + " threshold=" + str(threshold) + " elapsed_time=" + str(elapsed_time))
else:
	print("add params")

"""
Commando

python main.py 30 1000
python main.py 1000

"""