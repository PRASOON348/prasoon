list1 = [23,4,5,67,7]
list1.sort()
print(list1[-1])

max = list1[0]
for x in list1:
    if x > max:
        max = x
print(max)