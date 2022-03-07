coord = input()
xs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
def isInside(x, y):
    return x in xs and y > 0 and y < 9
def xEdit(x, n):
    res = str(chr(ord(x) + n))
    if res not in xs:
        return 'x'
    return res

def getAllCases(c):
    res = 0
    x = c[0]
    y = int(c[1])
    cases = [[1,2], [1,-2], [-1,2], [-1,-2], [2,1], [2,-1], [-2,1], [-2,-1]]
    for case in cases:
        rx = xEdit(x, case[0])
        ry = y + case[1]
        if isInside(rx, ry):
            res+=1
    return res

print(getAllCases(coord))