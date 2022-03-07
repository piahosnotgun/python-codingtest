import sys
import math

n=int(sys.stdin.readline().rstrip());

#c500: 500원, c100: 100원 ...

count = 0;

coins = [500,100,50,10]

for coin in coins:
    count+=n // coin
    n%=coin
print(count)