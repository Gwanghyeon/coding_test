# 제공된 배열 중 더해서 최대값 구하기
'''
n, m, k = map(int, input().split())
array = list(map(int, input().split()))

# max_count, max_add 의 초기값을 1로 두는 것이 중요!
max_count = 1
max_add = 1
result = 0
i = 0

array.sort(reverse=True)

print(array)

while max_count <= m:
    if max_add <= k:
        result += array[0]
        max_add += 1
    else:
        result += array[1]
        max_add = 1
    max_count += 1

print("the max value: ", result)


# The books's code

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):  # adding max_value
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

# practice
n, m, k = map(int, input().split())
array = list(map(int, input().split()))

array.sort(reverse=true)

result = 0

while true:
    for _ in range(k):
        if m == 0:
            break
        result += array[0]
        m -= 1
    if m == 0:
        break
    result += array[1]
    m -= 1
print(result)

# practice2

n, m, k = map(int, input().split())
array = list(map(int, input().split()))

result = 0
array.sort(reverse=True)

while True:
    for _ in range(k):
        if m == 0:
            break:
        result += array[0]
        m -= 1
    if m == 0:
        break
    result += array[1]
    m -= 1

print(result)

n,m,k=map(int, input().split())
array=list(map(int, input().split()))

result=0
array.sort(reverse=True)
first=array[0]
second=array[1]

while True:
    for _ in range(k):
        if m==0:
            break
        result+=first
        m-=1
    if m==0:
        break
    result+=second

print(result)

'''

# OR you can rewrite it in terms of recurrence relation

n, m, k = map(int, input().split())
array = list(map(int, input().split()))

counter_second = int(m//(k+1))
counter = (counter_second*k)+int(m % (k+1))
print(counter)
print(counter_second)
array.sort(reverse=True)
result = (array[0]*counter)+(array[1]*counter_second)

print(result)
