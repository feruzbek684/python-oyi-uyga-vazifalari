n = int(input("n : "))

sonlar = list(map(int, input("sonlar: ").split()))

def filter(lst):
    c = {}
    for i in lst:
        if i in c:
            c[i] += 1
        else:
            c[i] = 1
            
    son = set()
    
    for i,s in c.items():
        if s >= 2:
            son.add(i)
        
    return sorted(son)

sonlar = filter(sonlar)
print(sonlar)