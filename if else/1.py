son = int(input("son ni kiritng: "))
son1 = int(input("son ni kiritng: "))
son2 = int(input("son ni kiritng: "))
son3 = int(input("son ni kiritng: "))
son4 = int(input("son ni kiritng: "))
son5 = int(input("son ni kiritng: "))
juft  = 0
toq = 0
if son % 2 == 0:
    juft += 1
else:
    toq +=1
if son1 % 2 == 0:
    juft +=1
else:
    toq +=1
if son2 % 2 == 0:
    juft += 1
else:
    toq +=1
if son3  % 2 == 0:
    juft += 1
else:
    toq += 1
if son4  % 2 == 0:
    juft += 1
else:
    toq += 1
if son5  % 2 == 0:
    juft += 1
else:
    toq += 1

print("juft sonlar soni: ", juft)
print("toq sonlar soni: ", toq)
