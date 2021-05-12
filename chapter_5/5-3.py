n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        # 여기서의 리턴값은 사용하지 않는 다는게 핵심
        # 상,하,좌,우 인접 노드 방문처리만 진행
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x-1, y)
        dfs(x+1, y)
        # 처음 호출되는 true값만 의미가 있음!
        return True
    else:
        return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
