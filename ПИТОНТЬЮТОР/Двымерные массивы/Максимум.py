max_zn = 0
max_cord = [0, 0]
m = []
n = int(input().split()[0])
for i in range(1, n+1):
    a = list(map(int, input().split()))
    if i == 1:
        max_zn = a[0]
    m.append(a)
for i, zn1 in enumerate(m):
    for j, zn2 in enumerate(zn1):
        if zn2 == max_zn:
            if i < max_cord[0]:
                max_cord = [i, j]
            elif i == max_cord[0]:
                if j < max_cord[1]:
                    max_cord = [i, j]
            else:
                print("", end="")
        if zn2 > max_zn:
            max_zn = zn2
            max_cord = [i, j]
print(*max_cord)