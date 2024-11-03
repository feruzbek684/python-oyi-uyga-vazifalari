def qwerty(lst):
    ls =[]
    s = set()
    for i in lst:
        t = tuple(i)
        if t not in s:
            ls.append(i)
            s.add(t)
    return ls


list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
salom = qwerty(list)
print(salom)
