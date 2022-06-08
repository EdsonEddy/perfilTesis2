a = int(input())
while(a != 0):
    b = input()
    m = ''
    for i in range(len(b)):
        m = m + (b[len(b)-i-1]) 
    print(m)
    a = a - 1