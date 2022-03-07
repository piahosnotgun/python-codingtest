from collections import deque

m, n = map(int, input().split())
box = []

invalidCount = 0

queue = deque()

#시간 초과 원인
#bfs 알고리즘에 문제는 없었음. 익은 토마토의 좌표를 구해서 bfs를 돌리는것은 맞았으나,
#좌표를 배열에 넣고 다시 반복문을 돌릴 필요 없이 좌표를 구하는대로 queue에 넣고 바로 bfs돌려버리면 된거였음
#마지막에 반복문은 무조건 어쩔 수 없이 돌려야 하는 것이므로 생각하지 않되 반복문 사용 중에도 최대한으로 시간을 단축할 것.

for i in range(n):
    line = list(map(int, input().split()))
    box.append(line)
    for j in range(m):
        if line[j] == 1:
            queue.append(i)
            queue.append(j)
            invalidCount += 1
        if line[j] == -1:
            invalidCount +=1
if invalidCount == m*n:
    print(0)
    exit(0)
#bfs를 써서 인접 노드부터 탐색
#익은 토마토 기준으로 bfs돌리면 되는데
def isValid(x, y):
    return (x >= 0 and x < n) and (y >= 0 and y < m)

def bfs():
    global queue
    while len(queue) != 0:
        ax = queue.popleft()
        ay = queue.popleft() # x, y 좌표 하나씩 추출
            #ax, ay 좌표가 올바르고, 숫자가 0이나  -1이 아닌 경우, 인접한 노드에다가 자신의 숫자 + 1 대입
            #자신의 숫자 + 1이 인접한 노드의 숫자보다 큰 경우 대입하지 않음. 구문 종료. 0제외.
            #방향 정의
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        nextInt = box[ax][ay] + 1
        for i in range(4):
            nx = dx[i] + ax
            ny = dy[i] + ay
            if isValid(nx, ny):
                if box[nx][ny] == 0 or box[nx][ny] > nextInt:
                    queue.append(nx)
                    queue.append(ny)
                    box[nx][ny] = nextInt
bfs()
maxx = 0

for i in range(n):
    for j in range(m):
        num = box[i][j]
        if num == 0:
            print(-1)
            exit(0)
        maxx = max(num, maxx)
print(maxx -1)