from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

gX = n-1
gY = m-1

def bfs(startX, startY):
    xqueue = deque()
    yqueue = deque()
    
    xqueue.append(startX)
    yqueue.append(startY)
    
    while xqueue:
        x = xqueue.popleft()
        y = yqueue.popleft()
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for f in range(4):
            nx = x + dx[f]
            ny = y + dy[f]
            if (nx > n-1 or nx < 0) or (ny > m-1 or ny < 0) :
                continue
            if maze[nx][ny] == 1:
                xqueue.append(nx)
                yqueue.append(ny)
                maze[nx][ny] = maze[x][y] + 1
bfs(0, 0)
print(maze[gX][gY])