with open("football.txt", "r") as f:
    b = f.readlines()

for i in range(len(b)-1):
    print((b[i])[:-1])
print(b[len(b)-1])