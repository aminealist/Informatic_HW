from collections import Counter

def sieve(x):
    x = Counter(x)
    ret = []
    for i in x:
        if x[i] == 1:
           ret.append(i)
    return tuple(reversed(ret))


x = list(map(int, input().strip().split(" ")))
print(*sieve(x))
