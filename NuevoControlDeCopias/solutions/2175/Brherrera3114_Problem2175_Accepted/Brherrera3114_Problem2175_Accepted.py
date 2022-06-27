for x in range(int(input())):
    num = int(input())
    fibonacci = [0]
    n1,n2=1,0
    for i in range (100):
        if num in fibonacci:
            print(len(fibonacci)-1)
            break
        aux = n1 + n2
        fibonacci.append(aux)
        n1 = n2
        n2 = aux 
