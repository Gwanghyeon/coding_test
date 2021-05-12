from collections import deque

# dfs


def dfs(graph, visited, node):
    visited[node] = True
    print(node, end=' ')

    for i in graph[node]:
        if visited[i] != true:
            dfs(graph, visited, i)

# bfs


def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True

    while True:
        node = queue.popleft()
        print(node, end=" ")

        for i in graph[node]:
            if visited[i] != True:
                visited[i] = True
                queue.append(i)



#dfs
def dfs(graph, visited, node):
    visited[node]=True
    print(node, end=" ")

    for i in graph[node]:
        if visited[i]!=True:
           dfs(graph, visited, i) 

#bfs
def bfs(graph, visitied, start):
    queue=deque([start])

    while queue:
        node=queue.popleft()
        print(node, end=" ")

        for i in graph[node]:
            if visitied[i]!=True:
                queue.append(i)
                visitied[i]=True
