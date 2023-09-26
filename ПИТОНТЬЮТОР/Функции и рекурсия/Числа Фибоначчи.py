def fib(n, k=0, l=1, s=1):
    if n > 2:

        fib(n - 1, l, s, l + s)
    else:
        print(s)


fib(int(input()))
