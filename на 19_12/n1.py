from random import randint


def mtrx_crtng(n, m):
    a = []
    print(*[f"{i+1}  " for i in range(m)])
    for i in range(n):
        a.append([randint(-100, 100) for i in range(m)])
        print(*a[i])
    return a, n, m


a, n, m = mtrx_crtng(int(input("Введите кол-во строк:\n")), int(input("Введите кол-во столбцов:\n")))
print()

k = 0
for j in range(m):
    m = -101
    for i in a:
        if i[k] > m:
            m = i[k]
    print(f'максимальный элемент в {k+1} столбце: {m}')
    k += 1
