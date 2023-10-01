n = set([i + 1 for i in range(int(input()))])
b = ''

while b != "HELP":
    try:
        a = list(map(int, input().split()))
        b = input()
        if b == "NO":
            n -= set(a)
        else:
            n = n & set(a)
    except:
        break

print(*n)
