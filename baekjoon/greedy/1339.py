n = int(input())
words = [input() for i in range(n)]

digits = {}
replace = {}

for word in words:
    for i in range(len(word)):
        alphabet = word[i]
        digit = len(word) - i - 1
        if alphabet not in digits:
            digits[alphabet] = 10**digit
        else:
            digits[alphabet] += 10**digit 
sort = sorted(digits.items(), key=lambda item:item[1], reverse=True)
i = 9
res = 0
for item in sort:
    alphabet = item[0]
    part = item[1]
    if alphabet not in replace:
        replace[alphabet] = i
        i -= 1
    res += part * replace[alphabet]
print(res)