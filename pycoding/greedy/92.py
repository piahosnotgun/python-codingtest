import sys
n, m, k = map(int, sys.stdin.readline().split()) #n개의 자연수 배열, 최대 m번 더할 수 있음, 각 숫자는 k번까지만 나올 수 있음

ns = list(map(int, sys.stdin.readline().split()))

ns.sort(reverse=True)

if m == k:
    print(ns[0] * m)
else : #m > k
    res = (m//(k+1)) * ((ns[0] * k) + ns[1]) + (m%(k+1)) * ns[0]
    print(res)