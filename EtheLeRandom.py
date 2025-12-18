from random import randint as r

def randint(a, b):
    list = []
    for i in range(1000):
        list.append(r(a, b))



    return list[r(0, len(list)-1)]