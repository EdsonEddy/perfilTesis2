print('uno\tdos\ttres\tcuatro\tcinco\tseis\tsiete\tocho\tnueve\tdiez')
for i in range(1, 11):
	for j in range(1, 10):
		print(i*j, end='\t')
	print(i*10)