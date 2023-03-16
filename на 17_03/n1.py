print("___________1___________")
a = set(list(map(int, input("введите элементы списка через пробел").split(" "))))
b = set(list(map(int, input("введите элементы списка через пробел").split(" "))))
print(f"кол-во {len(a&b)},элементы:", *(a&b))
print(f"кол-во {len(a-b)},элементы:", *(a-b))
print(f"кол-во {len(b-a)},элементы:", *(b-a))
print("___________2___________")
a = (list(map(int, input("введите элементы списка через пробел \n").split(" "))))
b = set()
for i in a:
    print(i, "  ", end="")
print()
for i in a:
    if i in b:
        print("Yes", end="  ")
    else:
        print("No", end="  ")
        b.add(i)
