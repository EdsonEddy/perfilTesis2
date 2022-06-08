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

args.window_size = 4
args.kgram_len = 2

path1 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\dataset\\py-ofuscation-edit\\ofuscacion1_1\\ofuscacion1_1.py"
path2 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\dataset\\py-ofuscation-edit\\ofuscacion1_2\\ofuscacion1_2.py"
args.paths = [path1, path2]
try:
	res = local_moss(args)
except Exception as e:
	res = None
print("ofuscacion1=", res)

path1 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\dataset\\py-ofuscation-edit\\ofuscacion2_1\\ofuscacion2_1.py"
path2 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\dataset\\py-ofuscation-edit\\ofuscacion2_2\\ofuscacion2_2.py"
args.paths = [path1, path2]
try:
	res = local_moss(args)
except Exception as e:
	res = None
print("ofuscacion2=", res)

path1 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\dataset\\py-ofuscation-edit\\ofuscacion3_1\\ofuscacion3_1.py"
path2 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\dataset\\py-ofuscation-edit\\ofuscacion3_2\\ofuscacion3_2.py"
args.paths = [path1, path2]
try:
	res = local_moss(args)
except Exception as e:
	res = None
print("ofuscacion3=", res)

path1 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\dataset\\py-ofuscation-edit\\ofuscacion4_1\\ofuscacion4_1.py"
path2 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\dataset\\py-ofuscation-edit\\ofuscacion4_2\\ofuscacion4_2.py"
args.paths = [path1, path2]
try:
	res = local_moss(args)
except Exception as e:
	res = None
print("ofuscacion4=", res)

path1 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\dataset\\py-ofuscation-edit\\ofuscacion5_1\\ofuscacion5_1.py"
path2 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\dataset\\py-ofuscation-edit\\ofuscacion5_2\\ofuscacion5_2.py"
args.paths = [path1, path2]
try:
	res = local_moss(args)
except Exception as e:
	res = None
print("ofuscacion5=", res)

path1 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\dataset\\py-ofuscation-edit\\ofuscacion6_1\\ofuscacion6_1.py"
path2 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\dataset\\py-ofuscation-edit\\ofuscacion6_2\\ofuscacion6_2.py"
args.paths = [path1, path2]
try:
	res = local_moss(args)
except Exception as e:
	res = None
print("ofuscacion6=", res)

path1 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\dataset\\py-ofuscation-edit\\ofuscacion7_1\\ofuscacion7_1.py"
path2 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\dataset\\py-ofuscation-edit\\ofuscacion7_2\\ofuscacion7_2.py"
args.paths = [path1, path2]
try:
	res = local_moss(args)
except Exception as e:
	res = None
print("ofuscacion7=", res)

path1 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\dataset\\py-ofuscation-edit\\ofuscacion8_1\\ofuscacion8_1.py"
path2 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\dataset\\py-ofuscation-edit\\ofuscacion8_2\\ofuscacion8_2.py"
args.paths = [path1, path2]
try:
	res = local_moss(args)
except Exception as e:
	res = None
print("ofuscacion8=", res)
