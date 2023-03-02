from collections import Counter
print("______2______")
fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
sorted(fruits, reverse=1)
for i in fruits:
    print(i)
print("______4______")
numbers = {20, 6, 8, 18, 18, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 12, 8, 8, 10, 4, 2, 2, 2, 16, 20}
s = 0
k = 0
for i in numbers:
    s += i
    k += 1
print(int(s/k))
print("______6______")
a = Counter(input())
k = 0
for i in a:
    if not(a[i]==1):
        k+=1
        break
if k == 0:
    print("YES")
else:
    print("NO")
print("______7______")
a = input()
a += input()
a = set(sorted(set(a)))
if a == {'4', '0', '6', '7', '2', '3', '5', '9', '8', '1'}:
    print("YES")
else:
    print("NO")
print("______9______")
a, b, c = input().split(" ")
if set(a)==set(b)==set(c):
    print("YES")
else:
    print("NO")