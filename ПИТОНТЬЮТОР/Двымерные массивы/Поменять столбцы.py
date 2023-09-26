mtrx = []
n = int(input().split(" ")[0])
for i in range(n):
    a = list(map(int, input().split(" ")))
    mtrx.append(a)
a, b = map(int, input().split(" "))
for i, zn in enumerate(mtrx):
    mtrx[i][a], mtrx[i][b] = mtrx[i][b], mtrx[i][a]
for i in mtrx:
    print(*i)