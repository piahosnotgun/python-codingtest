n, m = map(int, input().split())

vertexes = []
graph = [list(map(int, input())) for __ in range(n)] #len: m

for i in range(n):
    for j in range(m):
        vertexes.append([i, j])

visited = [[False] * m for _ in range(n)]

res = 0

def search(x, y):
    global visited
    if (x < 0 or x >= n) or (y < 0 or y >= m):
        return
    if visited[x][y] == True:
        return
    visited[x][y] = True
    if graph[x][y] == 0:
        search(x-1, y)
        search(x, y-1)
        search(x+1, y)
        search(x, y+1)

for v in vertexes:
    x, y = v[0], v[1]
    if visited[x][y] == True or graph[x][y] == 1:
        continue
    res += 1
    search(x, y)
print(res)