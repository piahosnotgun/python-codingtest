n, m=map(int, input().split())
x, y, d=map(int, input().split())
lines = []
for i in range(n):
    line = list(map(int, input().split()))
    lines.append(line)
def getNextDirection(d):
    if d == 0:
        return 3
    return d - 1
def getNextCoord(x, y, d):
    if d == 0:
        return [x-1, y]
    if d == 1:
        return [x, y-1]
    if d == 2:
        return [x+1, y]
    if d == 3:
        return [x, y+1]
visited = []
visited.append([x, y])
cases = 1
def isOutside(c):
    global n, m
    return c[0] not in range(1, n-1) or c[1] not in range(1, m-1)
def isOcean(c):
    return lines[c[0]][c[1]] == 1
dirs = 0
while True:
    d = getNextDirection(d)
    nextCoord = getNextCoord(x, y, d)
    if dirs == 4:
        break
    if isOutside(nextCoord) or isOcean(nextCoord):
        dirs += 1
        continue
    if nextCoord in visited:
        dirs += 1
        continue
    visited.append(nextCoord)
    cases += 1
    x = nextCoord[0]
    y = nextCoord[1]
    dirs = 0
print(cases)