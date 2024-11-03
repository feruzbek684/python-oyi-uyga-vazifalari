def ls(lst):
    lst = [x for x in lst if x != 0] + [0] * lst.count(0)
    return lst


ls1 = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9 , 7, 1]
sonlar = ls(ls1)
print(sonlar)