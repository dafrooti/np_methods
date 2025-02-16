import numpy as np

list = [4, 5, 7, 2, 46, 16, 85, 9]
list2 = []

list_array = np.array(list)
print(list_array)
print(type(list_array))

for num in list:
    num = num * 2
    list2.append(num)

print(list2)
print(list_array*2)