from collections import Counter
n = int(input())
a = []
for i in range(n):
    for j in input().split():
        a.append(j)
print(len(Counter(a)))