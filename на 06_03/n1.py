from collections import Counter
from string import punctuation
print("_______4_______")
n = int(input())
a = set((input()))
for i in range(n-1):
    a = set((input()))&a
print(*sorted(list(map(int, a))))
print("_______6_______")
a = input().lower()
for i in punctuation:
    a = a.replace(i, " ")
a = set(a)
l = Counter(a)
k = 0
for i in l:
    if l[i]==1:
        k+=1
print(k)