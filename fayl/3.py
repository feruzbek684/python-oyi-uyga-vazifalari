f1 = open("aniqlash.txt", "w")
f1.write("#include<iosteram>int main(){ return 0; }")
f1.close()

f1 = open("aniqlash.txt", "rt")
harflar = f1.read()
soni =  0
for i in harflar:
    if i.isalpha():
        soni += 1
print(soni)
f1.close()