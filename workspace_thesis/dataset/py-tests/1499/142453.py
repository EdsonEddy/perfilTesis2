n=int(input())
v=list(map(int, input().split()))
v.append(0)
desdedonde=0
aux=[]
for i in range (desdedonde,n):
    if (v[i]<v[i+1]):
        desdedonde=desdedonde+1
        aux.append(v[i])
    else:
        break      
for i in range (desdedonde,n):
    if (v[i]==v[i+1]):
        desdedonde=desdedonde+1
        aux.append(v[i])
    else:
        break          
for i in range (desdedonde,n):
    if (v[i]>v[i+1]):      
        desdedonde=desdedonde+1
        aux.append(v[i])
    else:
        break
aux.append(0)              
if (aux==v):
    print ("SI")
else:
    print("NO")    