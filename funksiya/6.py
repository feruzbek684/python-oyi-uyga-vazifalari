import os; os.system("cls")
def listed(list1, list2):
    list3 = []
    max_list = max(len(list1), len(list2))
    
    for i in range(max_list):
        if i < len(list1):
            list3.append(list1[i])
        if i < len(list2):
            list3.append(list2[i])
    
    return list3

list1_a = [1, 2, 3]
list2_a = [11, 22, 33]
print("Input: list1 =", list1_a, "list2 =", list2_a)
print("Output:", listed(list1_a, list2_a))

list1_b = [1, 2, 3, 4, 5]
list2_b = [11, 22, 33]
print("Input: list1 =", list1_b, "list2 =", list2_b)
print("Output:", listed(list1_b, list2_b))

list1_c = [1, 2]
list2_c = [11, 22, 33, 44, 55]
print("Input: list1 =", list1_c, "list2 =", list2_c)
print("Output:", listed(list1_c, list2_c))
