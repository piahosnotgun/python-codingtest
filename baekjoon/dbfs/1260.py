from collections import deque
n, m, v = map(int, input().split())
graph = [[]]
for _ in range(n):
    graph.append([])
for i in range(m):
    j, k = map(int, input().split())
    if j not in graph[k]:
        graph[k].append(j)
    if k not in graph[j]:
        graph[j].append(k)

visited = [False * __ for __ in range(n+1)]
dfsRes = ""
def dfs(visited, v):
    global graph, dfsRes
    visited[v] = True
    
    dfsRes += str(v) + " "
    
    graph[v].sort()
    for x in graph[v]:
        if not visited[x]:
            dfs(visited, x)
dfs(visited, v)

print(dfsRes.strip())

bfsRes = ""

visited = [False * __ for __ in range(n+1)]
def bfs(visited, v):
    global graph, bfsRes
    
    queue = deque()
    queue.append(v)
    
    while len(queue) != 0:
        w = queue.popleft()
        visited[w] = True
        bfsRes += str(w) + " "
        graph[w].sort()
        for x in graph[w]:
            if not visited[x] and x not in queue:
                queue.append(x)
bfs(visited, v)
print(bfsRes.strip())