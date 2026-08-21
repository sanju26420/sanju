list1 = [1, 2, 2, 3, 4]
list2 = [2, 2, 4, 5]
list3 = [1, 2, 3, 4, 5]

duplicates = list(set(list1) & set(list2) & set(list3))

print(duplicates)
# [2, 4]
