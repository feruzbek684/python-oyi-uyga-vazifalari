def setlar(a, b):
    set = set(a)
    set1 = set(b)

    farq = set.difference(set1)
    farqlar = set1.difference(set)

    ls = list(farq.union(farqlar))
    ls.sort()
    return ls

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print("natija", setlar(a, b))
