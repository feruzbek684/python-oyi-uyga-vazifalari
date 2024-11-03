def funk(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    ls = list(set1.intersection(set2))
    lst = list(set1.union(set2))
    
    return ls, lst

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

ls,lst = funk(a, b)
print(a)
print(b)
print(ls)
