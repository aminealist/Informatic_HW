n, m = map(int, (input()).split(" "))
k = 1
l = -1
if m%2==1 :
    l = 1
for i in range(n):
    for j in range(m):
        if k == -1:
            if j == m-1:
                print("*")
                k *= l
            else:
                print("*", end=" ")
                k *= -1
        else:
            if j == m - 1:
                print(".")
                k*=l
            else:
                print(".", end=" ")
                k *= -1
