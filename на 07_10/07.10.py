for i in range(-150, 451):
    kk = 0
    for k in range(2, abs(i)):
        if i % k == 0:
            kk+=1
    if kk == 3:
        print(i)
