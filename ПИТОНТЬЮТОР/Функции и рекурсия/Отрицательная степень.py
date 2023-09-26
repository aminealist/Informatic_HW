def power(a, n):
    k = 1
    for i in range(abs(n)):
        k *= a
    return 1 / k if n < 0 else k


print(power(float(input()), int(input())))
