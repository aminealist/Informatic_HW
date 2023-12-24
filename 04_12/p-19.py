for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not (((w or y) == x) or ((w <= z) and (y <= w))):
                    print(y, x, z, w)
