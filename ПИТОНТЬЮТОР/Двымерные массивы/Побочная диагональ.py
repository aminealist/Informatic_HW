n = int(input())
k = n-1
for j in range(n):
    for i in range(n):
        if i<k:
            print(0, end="")
        elif i == k:
            print(1, end="")
        else:
            print(2, end="")
        if i != n-1:
            print(" ", end="")
        else:
            print("")
    k-=1