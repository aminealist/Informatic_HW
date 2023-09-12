from random import randint

a = []
for i in range(4):
    a.append([randint(-10, 10) for j in range(4)])
for i in a:
    print(*i)
s = 0
m = 11
for i in range(4):
    for j in range(4):
        if a[i][j] % 3 == 0:
            s += 1
        if j > i:
            if m > a[i][j]:
                m = a[i][j]
print(s)
print(m)
if s < 7:
    for i in range(4):
        a[i][1], a[i][2] = a[i][2], a[i][1]
for i in a:
    print(*i)
