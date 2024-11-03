soz = str(input("sozni kiritng: "))
harf = str(input("harfni kiritng: "))
bosh = ""
for i in range(len(soz)):
    if soz[i] == harf:
        bosh +=(soz[i].upper())
    else:
        bosh+=soz[i]
print("natija ", bosh)