print("___________1В___________")

for i in range(40, 71, 10):
    for k in range(1, 11):
        print(k+i, end=' ')
    print(" ")

print("___________2Б___________")

l = ''
for i in range(5):
    l += "1 "

for i in range(5):
    print(l)
    l = l[:-2]

print("___________3А___________")
for i in range(1 ,6):
    print((str(i) + " ") * i)

print("___________3Г___________")
l = ''
for i in range(5):
    l += "5 "
k = 1
for i in range(1, 4, 2):
    print(l)
    l = l[0:-2]
    print((str(k) + " ") * (5 - i))
    print("0 " * (5 - i))
    print((str(k) + " ") * (5 - (i+1)))
    l = l[0:-2]
    k += 1
