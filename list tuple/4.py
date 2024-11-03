matn = str(input("matn ni kiritng: "))
sozlar = matn.split()
ls = []

for i in sozlar:
    if len(i) % 2 != 0:
        ls.append(i[::-1])
    else:
        ls.append(i)
print("natija ==> ", ls)