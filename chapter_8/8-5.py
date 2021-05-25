# 최소 화폐개수

n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))

INF = 100001

d = [INF]*(m+1)

d[0] = 0
for i in range(n):
    for k in range(array[i], len(d)):
        d[k] = min(d[k], d[k-array[i]]+1)

print(d[m])
