codigo=input().split("0")
while "" in codigo:
    codigo.remove("")
resp=""
for i in codigo:
    resp=resp+str(len(i))
print(resp)