n=int(input())
c=0
#para convertir cualquier decimal en binario
binario=''
while n//2 != 0:
    binario=str(n %2)+binario
    n=n//2
x=int(str(n%2)+binario)
# para oconvertir , etc
while x>0:
    x=x//10
    c=c+1
print(c)
#de ----n veces para convertir decimal binario bits
n=int(input())
while n >0:
    c = 0
    binario = ''
    while n // 2 != 0:
        binario = str(n % 2) + binario
        n = n // 2
    x = int(str(n % 2) + binario)
    while x > 0:
        x = x // 10
        c = c + 1
    print(c)
    n=int(input())