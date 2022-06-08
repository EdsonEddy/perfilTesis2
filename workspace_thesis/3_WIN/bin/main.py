import argparse
from timeit import default_timer

parser = argparse.ArgumentParser()
parser.add_argument("paths", nargs="*") # TODO more details
parser.add_argument("--reference", "-r", action="append")
parser.add_argument( "--language", "-l", default="python")
parser.add_argument("--window_size", "-w", default=10, type=int)
parser.add_argument("--kgram_len", "-k", default=1, type=int)
parser.add_argument("--collision_threshold", "-c", default=10, type=int)
parser.add_argument("--output_size", "-s", default="short", choices=["short", "medium", "long"])
parser.add_argument("--top", "-t", default=15, type=int)
parser.add_argument("--silent", action="store_true")
parser.add_argument("--pre_lines", default=5, type=int)
parser.add_argument("--post_lines", default=5, type=int)


args = parser.parse_args()

from local_moss_edited import local_moss
import sys
import os

start_time = default_timer()

save_path = args.paths[0]
path_source = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\dataset\\py-tests-edit\\"
path1 = path_source + args.paths[0]
n = len(os.listdir(path1))
precision = [[0 for _ in range(n)] for _ in range(n)]

for idx, i in enumerate(os.listdir(path1)):
	source = path1 + "\\" + i + "\\" + i + ".py"
	for idy, j in enumerate(os.listdir(path1)):
		destiny = path1 + "\\" + j + "\\" + j + ".py"
		if idx == idy:
			precision[idx][idx] = 100
		else:
			args.paths = [source, destiny]
			try:
				coef = local_moss(args)
			except Exception as e:
				coef = 0
			precision[idx][idy] = coef
			precision[idy][idx] = precision[idx][idy]

path_out1 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\" + save_path + "_WIN_W_" + str(args.window_size) +"_K_"+ str(args.kgram_len) + "_PRECISION.csv"
import numpy as np
x1 = np.asarray(precision)
np.savetxt(path_out1, x1, delimiter=',')

elapsed_time = default_timer() - start_time
path_out2 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\execution_time.txt"
with open(path_out2, "a") as myfile:
    myfile.write("\n" + save_path + " WIN window=" + str(args.window_size) +" kgrams="+ str(args.kgram_len) + " elapsed_time=" + str(elapsed_time))

"""
command

python main.py -w 1 -k 1 1275

-k, default=5, -w, default=15
python main.py 1275

"""
