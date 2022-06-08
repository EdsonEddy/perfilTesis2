from local_moss_edited import local_moss
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("paths", nargs="*") # TODO more details
parser.add_argument("--reference", "-r", action="append")
parser.add_argument( "--language", "-l", default="python")
parser.add_argument("--window_size", "-w", default=15, type=int)
parser.add_argument("--kgram_len", "-k", default=5, type=int)
parser.add_argument("--collision_threshold", "-c", default=10, type=int)
parser.add_argument("--output_size", "-s", default="short", choices=["short", "medium", "long"])
parser.add_argument("--top", "-t", default=15, type=int)
parser.add_argument("--silent", action="store_true")
parser.add_argument("--pre_lines", default=5, type=int)
parser.add_argument("--post_lines", default=5, type=int)
args = parser.parse_args()


path1 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\dataset\\py-tests-edit\\1003\\137797\\137797.py"
path2 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\dataset\\py-tests-edit\\1003\\145676\\145676.py"
args.paths = [path1, path2]


percentages = [(10,1),(10,2),(10,3),(10,4),(10,5)]

for threshold in percentages:
	w = threshold[0]
	k = threshold[1]
	args.window_size = w
	args.kgram_len = k
	try:
		precision = local_moss(args)
	except Exception as e:
		precision = 0
	print("win=", w, " kgram=", k, " precision=", precision)