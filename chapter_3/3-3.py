n, m = map(int, input().split())

result = 0

for _ in range(n):
    array = list(map(int, input().split()))
    min_value = min(array)
    result = max(min_value, result)

print(result)
