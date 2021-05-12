'''
n = int(input())


array = dict()

for _ in range(n):
    data = input().split()
    array[data[0]] = int(data[1])

array_result = sorted(array, key=lambda array: array[1])

print(array)

print(array_result)
'''

# the answer

n = int(input())

array = []
for _ in range(n):
    data = input().split()
    array.append((data[0], int(data[1])))

array = sorted(array, key=lambda array: array[1])

print(array)

for data in array:
    print(data[0], end=' ')
