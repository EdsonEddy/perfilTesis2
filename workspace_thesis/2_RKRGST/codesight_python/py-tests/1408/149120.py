Alvaro=[ "A", "B", "C"]
Edwin=["B", "A", "B", "C"]
Gabriel=["C", "C", "A", "A", "B", "B"]
H=0
J=0
K=0
x=int(input())
pregG=input()
for i in range(x):
    if Alvaro[i%len(Alvaro)]==pregG[i]:
        H+=1
    if Edwin[i%len(Edwin)]==pregG[i]:
        J+=1
    if Gabriel[i%len(Gabriel)]==pregG[i]:
        K+=1
notas=[H,J,K]
m=max(H,J,K)
cali=[]
if m==notas[0]:
    cali.append("Alvaro")
if m==notas[1]:
    cali.append("Edwin")
if m==notas[2]:
    cali.append("Gabriel")
print(m)
for k in range(len(cali)):
    print(cali[k])