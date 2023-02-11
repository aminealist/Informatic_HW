n = int(input())

for i in range(n):
    for j in range(n):
        if (i+j == n-1) or (i == j) or (i == n//2) or (j == n//2):
            if j == n-1:
                print("*")
            else:
                print("*", end=" ")
        else:
            if j == n - 1:
                print(".")
            else:
                print(".", end=" ")