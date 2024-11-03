ls = [
    [1,"Jean Castro", "V"],
    [2,"Lule Powell ", "V"],
    [3,"Brian Howell", "VI"],
    [4,"Lynne Foster", "VI"],
    [5,"Zachary Simon", "VII"]
]

dic = {i[0]: [i[1], i[2]] for i in ls}
print(dic)