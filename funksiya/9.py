n = int(input("n: "))

sonlar = list(map(int,input("sonlar: ").split()))

def ikki(lst):
    d = {}
    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    son = []
    for i in lst:
        if d[i] > 1:
            son.append(i)
    
    return son

sonlar = ikki(sonlar)
print(sonlar)