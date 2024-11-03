d = {1: "ABC", 2:"DEF", 3:"GHI", 4:"JKL", 5:"MNO"}

keylar = list(d.keys())
for i in range(1, len(keylar), 2):
    d[keylar[i]], d[keylar[i - 1]] = d[keylar[i - 1]], d[keylar[i]]

print(d)