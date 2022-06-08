from sys import stdin
primo = ['2', '3', '5', '7']
for line in stdin:
    for casa in range(int(line)):
        nCasa = input()
        nNum = ''
        for i in range(len(nCasa)):
            if nCasa[i] in primo:
                nNum = nNum + nCasa[i]
        if nNum == '':
            print(0)
        else:
            print(nNum)
