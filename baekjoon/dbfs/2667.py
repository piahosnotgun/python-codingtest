n = int(input())

amap = [list(map(int, input())) for _ in range(n)]

cpx = [0]#인덱스 1부터 넣어야함. 아파트 단지 => 아파트 수

num = 2
def dfs(x, y, i):
    vx = [1, 0, -1, 0]
    vy = [0, 1, 0, -1]
    
    if isValid(x, y) and amap[x][y] == 1:
        amap[x][y] = i
        
        k = i - 1 #진짜 단지 번호
        if k >= len(cpx):
            cpx.append(0)
        cpx[k] += 1
        
        for j in range(4):
            nx = vx[j] + x
            ny = vy[j] + y
            dfs(nx, ny, i)

def isValid(x, y):
    return (x < n and x >= 0) and (y < n and y >= 0)

for x in range(n):
    for y in range(n):
        if amap[x][y] == 1 and isValid(x, y):
            dfs(x, y, num)
            num += 1
            
print(len(cpx) - 1)
cpx.sort()
for i in range(len(cpx)):
    if cpx[i] != 0:
        print(cpx[i])