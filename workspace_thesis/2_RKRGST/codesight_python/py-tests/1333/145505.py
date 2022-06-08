#word ="banana"
word = input()
n = 0
lo = []
while n<len(word):
    lo.append(word[n:])
    #print(word[n:])
    n+=1
    if n ==len(word):
        break
m = sorted(lo)
print("\n".join(m))