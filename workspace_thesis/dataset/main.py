import os, sys
import numpy as np
import pygments.token
import pygments.lexers

def meansures(arr):
	arr = np.array(arr)
	N = len(arr)
	mean = np.mean(arr)
	var = sum([(xi - mean) ** 2 for xi in arr]) / (N - 1)
	desv_std = mean ** 0.5
	coef_var = desv_std / mean
	return [mean, var, desv_std, coef_var]

path_source = "py-tests"
dirs = open("files_list.txt", "r")

try:
	os.remove("results_lines.txt")
	os.remove("results_tokens.txt")
except Exception as e:
	raise e

res1 = open("results_lines.txt", "w")
res2 = open("results_tokens.txt", "w")
for directory in dirs:
	path = path_source + "\\" + directory
	path = path.strip()

	arr_lines_cnt = []
	arr_tokens_cnt = []
	for element in os.listdir(path):
		path_destiny = path + "\\" + element
		files = open(path_destiny, "r")
		# lines
		lines_cnt = 0
		for line in files:
			lines_cnt += 1
		arr_lines_cnt.append(lines_cnt)
		files.close()
		# tokens
		files = open(path_destiny, "r")
		text = files.read()
		files.close()
		lexer = pygments.lexers.guess_lexer_for_filename(path_destiny, text)
		tokens = lexer.get_tokens(text)
		tokens = list(tokens)
		lenT = len(tokens)
		tokens_cnt = 0
		for i in range(lenT):
			if tokens[i][0] == pygments.token.Name and not i == lenT - 1 and not tokens[i + 1][1] == '(':
				tokens_cnt += 1
			elif tokens[i][0] in pygments.token.Literal.String:
				tokens_cnt += 1
			elif tokens[i][0] in pygments.token.Name.Function:
				tokens_cnt += 1
			elif tokens[i][0] == pygments.token.Text or tokens[i][0] in pygments.token.Comment:
				pass
			else:
				tokens_cnt += 1
		arr_tokens_cnt.append(tokens_cnt)

	lines_result = meansures(arr_lines_cnt)
	lines_result = [round(_, 2) for _ in lines_result]
	lines_result = str(lines_result)
	lines_result = lines_result[1:len(lines_result) - 1]
	lines_result = lines_result.replace(", ", " & ")

	tokens_result = meansures(arr_tokens_cnt)
	tokens_result = [round(_, 2) for _ in tokens_result]
	tokens_result = str(tokens_result)
	tokens_result = tokens_result[1:len(tokens_result) - 1]
	tokens_result = tokens_result.replace(", ", " & ")

	res1.write(directory.strip() + " & " + lines_result + "\\\\ \\hline\n")
	res2.write(directory.strip() + " & " + str(tokens_result) + "\\\\ \\hline\n")
dirs.close()
res1.close()
res2.close()