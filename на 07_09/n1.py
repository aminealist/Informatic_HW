from random import randint

a = []
for i in range(8):
    a.append(randint(-10, 10))
print(*a)
print()
s = 0
for i in a:
    if i % 2 == 0:
        s += i
m = a.index(min(a))
print(s)
print(m)
if s>m:
    for i in range(8):
        if i == 2:
            print(0, end=" ")
        print(a[i], end=" ")
else:
    print(*a)