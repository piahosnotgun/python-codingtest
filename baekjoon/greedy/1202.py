import heapq

n, k = map(int, input().split())

jewels = []
bags = []

for i in range(n):
    w, v = map(int, input().split())
    heapq.heappush(jewels, (-v, v, w)) # 가격 순으로 정렬. 높은 값일수록 부모가 되는 최대힙 구조.
for i in range(k):
    w = int(input())
    heapq.heappush(bags, w)
    
res = 0
while len(jewels) > 0 and len(bags) > 0:
    j = heapq.heappop(jewels)
    jv = j[1]
    jw = j[2]
    
    bw = bags[0][1]
    if jw > bw:
        continue
    heapq.heappop(bags)
    res += jv

print(res)