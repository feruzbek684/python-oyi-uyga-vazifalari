sonlar = list(map(int, input("soni kiritng: ").split()))
even_count = sum(1 for i in sonlar if i % 2 == 0)

if even_count >= 2:
    print(list(map(str, sonlar)))
else:
    print(0)
