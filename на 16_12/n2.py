from random import randint
n = int(input(" введитье размер квадратной матрицы \n"))
s = 0
a=[]

for i in range(n):
    a.append([randint(-100, 100) for i in range(n)])

for i in a:
    print(*i)
print("sum диагонали")
for i in range(n):
    s+=a[i][i]

print(s)


print("сред. побочной диагонали")

s=0

for i in range(n):
    s+=a[i][-1-i]

print(s/n)