import numpy as np
def my_func(source):
	data = np.loadtxt(source, delimiter=',')
	m, n = np.shape(data)
	return np.sum(data) / (m * n)

source1 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\1275_RKRGST_T_20_PRECISION.csv"
source2 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\1407_RKRGST_T_20_PRECISION.csv"
source3 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\1588_RKRGST_T_20_PRECISION.csv"
source4 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\1222_RKRGST_T_20_PRECISION.csv"
source5 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\1089_RKRGST_T_20_PRECISION.csv"
print("A", "RKRGST", my_func(source1))
print("B", "RKRGST", my_func(source2))
print("C", "RKRGST", my_func(source3))
print("D", "RKRGST", my_func(source4))
print("E", "RKRGST", my_func(source5))

source6 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\1275_SCED_D_100_PRECISION.csv"
source7 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\1407_SCED_D_100_PRECISION.csv"
source8 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\1588_SCED_D_100_PRECISION.csv"
source9 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\1222_SCED_D_100_PRECISION.csv"
source10 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\1089_SCED_D_100_PRECISION.csv"
print("A", "SCED", my_func(source6))
print("B", "SCED", my_func(source7))
print("C", "SCED", my_func(source8))
print("D", "SCED", my_func(source9))
print("E", "SCED", my_func(source10))

source11 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\1275_WIN_W_4_K_2_PRECISION.csv"
source12 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\1407_WIN_W_4_K_2_PRECISION.csv"
source13 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\1588_WIN_W_4_K_2_PRECISION.csv"
source14 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\1222_WIN_W_4_K_2_PRECISION.csv"
source15 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\1089_WIN_W_4_K_2_PRECISION.csv"
print("A", "WIN", my_func(source11))
print("B", "WIN", my_func(source12))
print("C", "WIN", my_func(source13))
print("D", "WIN", my_func(source14))
print("E", "WIN", my_func(source15))

