for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not (x and (y <= z) or w) and w == 0:
                    print(z, w, x, y)
