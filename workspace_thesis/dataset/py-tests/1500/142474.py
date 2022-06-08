test_cases = int(input())
l=list(input().split())
count=0
sw=True
for item in reversed(l):
    if item !=   l[count]:
        sw=False
    count+=1
if sw==False:
    print("NO")
else:
    print("SI")
