n = int(input(" введитье n \n"))
m = int(input(" введитье m \n"))
a=[]
k=10
for i in range(n):
    b=[]
    for j in range(m):
       b.append((i+1)*10+j)
    a.append(b)
print()
for i in a:
    print(*i)