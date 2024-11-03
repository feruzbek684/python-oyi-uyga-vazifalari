def chiqar(lst, ls):
    ls = ls.lower()
    son = []
    for i in lst:
        if i[0].lower() == ls:
            son.append(i)
    return son

qwerty = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
for j in ['a', 'd', 'w']:
    print(f"{j} bilan boshlandiganlar")
    print(chiqar(qwerty, j))