n = int(input())
count = 0
for i in range(n): #i시 *분 *초
    if i==3 or i==13 or i==23:
        count += 60 * 60
        continue
    cases = [3, 13, 23, 33, 43, 53, 30, 31, 32, 34, 35, 36, 37, 38, 39]
    for m in range(60):
        for s in range(60):
            if m in cases or s in cases:
                count+=1
print(count)