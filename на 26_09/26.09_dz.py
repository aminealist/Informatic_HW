print('______________2______________')


a = int(input())
b = int(input())
k=1
if a < 0:
    k *= -1
    a *= -1
if b < 0:
    k *= -1
    b *= -1
l = 0
for i in range(a):
    l+=b
print(l*k)


print('______________6______________')


a=input("")
l = 0
for i in range(len(a)):
    if a.count(a[i]) > 1:
        l += 1
if l > 0:
    print('да')
else:
    print('нет')
