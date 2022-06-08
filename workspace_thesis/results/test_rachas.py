import numpy as np
def my_func(source1, source2):
	data1 = np.loadtxt(source1, delimiter=',')
	data2 = np.loadtxt(source2, delimiter=',')
	name1 = source1.split("\\")[-1].replace(".csv","")
	name2 = source2.split("\\")[-1]
	target_path = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\mix_rkrgst_win\\" + name1 + name2

	m, n = np.shape(data1)
	t = [[0 for _ in range(n)] for _ in range(m)]
	for i in range(m):
		for j in range(n):
			t[i][j] = max(data1[i][j], data2[i][j])

	x1 = np.asarray(t)
	np.savetxt(target_path, x1, delimiter=',')

source1 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\1275_RKRGST_T_20_PRECISION.csv"
source2 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\1275_WIN_W_4_K_2_PRECISION.csv"
my_func(source1, source2)

source1 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\1407_RKRGST_T_20_PRECISION.csv"
source2 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\1407_WIN_W_4_K_2_PRECISION.csv"
my_func(source1, source2)

source1 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\1588_RKRGST_T_20_PRECISION.csv"
source2 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\1588_WIN_W_4_K_2_PRECISION.csv"
my_func(source1, source2)

source1 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\1222_RKRGST_T_20_PRECISION.csv"
source2 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\1222_WIN_W_4_K_2_PRECISION.csv"
my_func(source1, source2)

source1 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\1089_RKRGST_T_20_PRECISION.csv"
source2 = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\1089_WIN_W_4_K_2_PRECISION.csv"
my_func(source1, source2)