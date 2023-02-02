#def tpl_sort1(x):
   # if len([i for i in x if not(isinstance(i, int))]) != 0:
     #   return x
    #else:
        #return tuple(sorted(x))

def tpl_sort(x):
    try:
        x = tuple(map(int, x))
        return tuple(sorted(x))
    except:
        return x

x = input().strip().split(" ")
print(*x)
print(*tpl_sort(x))