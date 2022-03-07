from collections import deque

n, m=map(int, input().split())
maze = [list(map(int, input())) for __ in range(n)]
count = 1

queue = deque()
queue.append(0)
queue.append(0) # 시작점 1, 1, 출구는 n, m => 0,0 n-1, m-1

def bfs():
    global queue
    
    while len(queue) != 0:
        x = queue.popleft()
        y = queue.popleft()
        dx = [-1,0, 1, 0]
        dy = [0, -1, 0, 1]
        
        nextInt = maze[x][y] + 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if (nx >= 0 and nx < n) and (ny >= 0 and ny < m): #nx, ny좌표가 valid한 경우
                if maze[nx][ny] == 0:
                    continue
                if maze[nx][ny] == 1:
                    maze[nx][ny] = nextInt
                    queue.append(nx)
                    queue.append(ny)
bfs()
print(maze)
print(maze[n-1][m-1])