def power(a, n, k=1, s = 0):
    if s != n:
        s+=1
        return power(a, n, k*a, s)
    else:
        print(k)


power(float(input()), int(input()))
