n = int(input("soni kiritng: "))
soni = 0
ikki = ""
while n > 0:
    if n % 2 == 0:
        ikki = '0' + ikki
        soni += 1
    else:
        ikki = '1' + ikki
    n //= 2
print("0 lar soni ", soni)