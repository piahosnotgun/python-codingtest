n, m = map(int, input().split())
cakes = list(map(int, input().split()))

cakes.sort()

h = max(cakes)

def search(target):
    global cakes
    start = 0
    end = len(cakes) - 1
    while start <= end:
        mid = (start + end) // 2
        if cakes[mid] == target:
            return mid
        elif cakes[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

lastIndex = len(cakes) - 1

for i in range(h, -1, -1):
    index = search(i)
    if index == None:
        summ = 0
        for j in range(lastIndex, len(cakes)):
            summ += cakes[j] - i
        if summ >= m:
            print(i)
            exit(0)
    else:
        lastIndex = index
        summ = 0
        for j in range(index, len(cakes)):
            summ += cakes[j] - i
        if summ >= m:
            print(i)
            exit(0)