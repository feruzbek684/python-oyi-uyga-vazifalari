ls = [1,2,3]
ls1 = [61,228,9]

ls_sort = sorted(map(str, ls), reverse=True)
ls_sort1 = sorted(map(str, ls1), reverse=True)
son = ''
for i in ls_sort:
    son += i
son1 = ''
for i in ls_sort1:
    son1 += i
print(son)
print(son1)