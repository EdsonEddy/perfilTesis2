casos = int(input())
for x in range(casos):
    word = input()
    nn = ''
    for i in word:
        nn = i + nn
    print(nn)