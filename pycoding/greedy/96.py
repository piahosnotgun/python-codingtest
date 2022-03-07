n, m=map(int, input().split())
lines = [[0] * n for _ in range(m)]

for i in range(n): #O(n)
    line = list(map(int, input().split()))
    for j in range(m):
        lines[j][i] = line[j]
row = -1
biggest = -1

for k in range(m):
    lines[k].sort()
    smallest = lines[k][0]
    if smallest > biggest:
        row = k
        biggest = smallest
print(row+1)