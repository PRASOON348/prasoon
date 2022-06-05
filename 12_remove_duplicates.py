#remove the duplicate values in a list
list1 = [2,3,4,54,2,2,2,2,2,2,2,2,2,22,2,3,4,5,56,7,7,3]
list2 = []

for v in list1:
    if v not in list2:
        list2.append(v)
print(list2)
