n = int(input())
routes = input().split()
x = 1
y = 1
for r in routes:
    if r == 'R':
        if y+1 <= n:
            y += 1
    if r == 'L':
        if y-1 >= 1:
            y -= 1
    if r == 'D':
        if x+1 <= n:
            x += 1
    if r == 'U':
        if x-1 >= 1:
            x -= 1
print(str(x) + " " + str(y))