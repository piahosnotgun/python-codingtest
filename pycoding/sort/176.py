data = [7,1,3,3,4,3,7,5,2,0,0,0]

arr = [0] * (max(data)+1)

for i in data:
    arr[i]+=1

res = []
for i in range(len(arr)):
    for j in range(arr[i]):
        res.append(i)
print(res)
data.sort()
print(data)