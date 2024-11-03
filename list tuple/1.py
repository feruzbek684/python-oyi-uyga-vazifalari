lst = [1, 2, 33, 5, 6, 7, 7]
n = int(input("soni kiritng: "))
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == n:
            print(f"inndexi{i}, {j}, = {n}")