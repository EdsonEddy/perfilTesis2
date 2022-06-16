N = int(input())
cabeza = "   *   "
medio1 = "  /#\  "
medio2 = " /###\ "
base   = "___#___"
c = cabeza
m1 = medio1
m2 = medio2
b = base
while N > 1:
    c = c + cabeza
    m1 = m1 + medio1
    m2 = m2 + medio2
    b = b + base
    N = N - 1
print(c)
print(m1)
print(m2)
print(b)
