import pandas as pd

# s1 = pd.Series([10, 20, 30, 40])
# s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

# print(s1)
# print(s2)

# marks = pd.Series([85, 90, 78], index=['Math', 'Physics', 'Chemistry'])

# print(marks['Math'])
# print(marks[['Math', 'Chemistry']])

# scores = pd.Series([45, 67, 89, 34, 90])

# passed = scores[scores > 60]
# print(passed)

# data = pd.Series([10, None, 30, None])

# print(data.isnull())
# print(data.fillna(0))

names = pd.Series(['Alice', 'abob', 'CHARLIE'])

print(names.str.lower())
print(names.str.contains('a'))

# data=pd.Series([700, 150, 300],index=['Laptop', 'Mouse', 'Keyboard'])
# print("The price of 'Laptop'is",data['Laptop'])
# print("The first two products",data[0:2])

# data=pd.Series([85, None, 92, 45, None, 78, 55])
# print("values are missing",data.isnull())
# print(" values with a default score of 0 using",data.fillna(0))
# print("values greater than 60",data[data>60])

# data=pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
# print(data.str.strip())
# print(data.str.lower())
# print(data.str.contains('a'))
 