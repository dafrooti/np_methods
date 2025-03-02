import numpy as np

# list = [4, 5, 7, 2, 46, 16, 85, 9]
# list2 = []

# list_array = np.array(list)
# print(list_array)
# print(type(list_array))

# for num in list:
#     num = num * 2
#     list2.append(num)

# print(list2)
# print(list_array*2)

# Making Arrays
# list_of_zeros = np.zeros(10, object)
# print(list_of_zeros)
# print(list_of_zeros.ndim)
# print(list_of_zeros.shape)
# print(list_of_zeros.size)
# print(list_of_zeros.dtype)

# list_of_one = np.ones((10, 10), int)
# print(list_of_one)
# print(list_of_one.ndim)
# print(list_of_one.shape)
# print(list_of_one.size)
# print(list_of_one.dtype)

# array1 = np.arange(4, 53, 4)
# array1 = np.random.permutation(array1)

# print(array1)

# array2 = np.random.uniform(5, 30, 2)
# print(array2)

# array3 = np.linspace(1, 10, 4)
# print(array3)

# array4 = np.random.permutation(np.arange(1, 101)).reshape(20, 5)
# print(array4)

# array5 = np.random.randint(2, 50, 10)
# array6 = np.sort(array5)

# print(array6)

# array7 = np.array([5, 64, 4, 91, 77, 37])
# array8 = array7.reshape(3, 2)

# print(array8)
# print(array7[3])
# print(array7[2:4])
# print(array8[0:2, 0])
# print(array7[[0,5]])

array9 = np.random.randint(1, 100, 16).reshape(4, 4)
array10 = np.random.randint(1, 50, 16).reshape(4, 4)

print(array9)
# print(array10)
# print(array9-array10)

def solve(x):
    return 5*x + 3

y = solve(array9)
# print(y)

array11 = array9[array9 > 15]
print(array11)
