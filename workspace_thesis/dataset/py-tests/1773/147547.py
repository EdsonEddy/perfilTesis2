def lcs(str1, str2):
    lcs=[]
    c = len(str2)+1
    f = len(str1)+1
    for f in range(f+1):
        lcs.append([0]*(c+1))
    for i in range(f):
        for j in range(c):
            if i == 0 or j == 0:
                lcs[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                lcs[i][j] = 1 + lcs[i - 1][j-1]
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j-1])
    return lcs[len(str1)][len(str2)]

ite=1
while ite != 0:
    str1 = input().strip().replace(' ', '')
    str2 = input().strip().replace(' ', '')
    #" ".join(str1.split())
    #" ".join(str2.split())
    #str1.replace(' ', '')
    #str2.replace(' ', '')
    a = lcs(str1, str2)
    prom = (a/min(len(str1), len(str2)))*100
    print(f"Compatibilidad: {prom:.2f} %")