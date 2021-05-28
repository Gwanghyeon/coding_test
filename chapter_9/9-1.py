import sys

input = sys.stdin.readline()
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
visited = [False]*(n+1)
distance = [INF]*(n+1)

for _ in range(n):
    a, b, c = map(int, input().split())
    # a에서 b까지 가는 비용 c
    graph[a].append((b, c))


def get_shortest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = 0

    for node in graph[start]:
        distance[node[0]] = node[1]

    for _ in range(n-1):
        min_index = get_shortest_node()
        visited[min_index] = True
        for node in graph[min_index]:
            cost = distance[min_index]+node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost


dijkstra(start)
