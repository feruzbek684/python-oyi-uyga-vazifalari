son = int(input("son ni kiritng: "))
son1 = int(input("son ni kiritng: "))
son2 = int(input("son ni kiritng: "))

if son > son1 and son1 < son2:
    print("ortacha qiymat", son1)
    
if son1 > son and son < son2:
    print("ortacha qiymat ", son)

if son > son2 and son2 < son1:
    print("ortacha qiymat ", son2)
