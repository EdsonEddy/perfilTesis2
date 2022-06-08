import numpy as np
import pandas as pd

name = "1588"

pre = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\mix_rkrgst_win\\"+name+"_RKRGST_T_20_PRECISION"+name+"_WIN_W_4_K_2_PRECISION.csv"
pos = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\"+name+"_SCED_D_100_PRECISION.csv"
target_path = "C:\\Users\\ACCESO\\Desktop\\experiments_file\\results\\mix_rkrgst_win\\"+name+"_Wilcoxon.xlsx"
data1 = np.loadtxt(pre, delimiter=',')
data2 = np.loadtxt(pos, delimiter=',')
m, n = np.shape(data1)
t = []
for i in range(m):
	for j in range(n):
		if i > j:
			t.append([data1[i][j], data2[i][j]])
df1 = pd.DataFrame(t)
df1.to_excel(target_path)