n, k = map(int, input().split())

def first(n):
    return n - 1
def second(n, k):
    return n//k

count = 0
while(n!=1):
    if n%k != 0:
        n = first(n)
    else:
        n = second(n, k)
    count+=1
print(count)