while 1>0:
    numeroDeDatos=int(input())
    nums= input().split()
    ultimoDigito=nums[-1]
    cont=0
    #print(nums)
    for i in nums:
        #print(i)
        if i ==ultimoDigito:
            cont+=1
    print(cont)