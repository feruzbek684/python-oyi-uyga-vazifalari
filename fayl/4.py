
f1 = open("aniqlash.txt", "rt")
harflar = f1.read()
soni =  0
for i in harflar:
    if i.isdigit():
        soni += 1
print(soni)
f1.close()