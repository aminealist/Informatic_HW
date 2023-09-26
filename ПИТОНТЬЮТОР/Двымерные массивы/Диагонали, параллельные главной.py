n = int(input())
lst_el = 0
a = [i for i in range(n)]
for i in range(n):
    print(*a)
    lst_el +=1
    for i in range(n-1,0,-1):
        a[i] = a[i-1]
    a[0]= lst_el