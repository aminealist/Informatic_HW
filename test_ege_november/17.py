with open("17.txt") as f:
    a = list(map(int, f.read().strip().split()))
b = [i for i in a if i % 2 == 0]
sr = sum(b) / len(b)
print(sr)
k = 0
for i in range(len(a) - 1):
    if (a[i] % 3 == 0 and a[i + 1] < sr) or (a[i + 1] % 3 == 0 and a[i] < sr):
        k += 1
print(k)
