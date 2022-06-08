c=int(input())
for l in range(c):
    num=input()
    nnum = ''
    for i in range(len(num)):
        if num[i] == '2' or num[i] == '3' or num[i] == '5' or num[i] == '7':
            nnum = nnum + str(num[i])
    if nnum != '':
        print(nnum)
    else:
        print('-1')
