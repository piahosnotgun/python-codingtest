s = input()
t = input()

def reverse():
    global t
    tmp =""
    for i in range(len(t)-1, -1, -1):
        tmp += t[i]
    t = tmp
    
def first(): #뒤에서 A 제거
    global t
    t = t[0:len(t)-1]
    
def second(): #뒤에서 B 제거후 뒤집기
    global t
    t = t[0:len(t)-1]
    reverse()
valid = 1
while s != t:
    if t[len(t)-1] == "A":
        first()
    elif t[len(t)-1] == "B":
        second()
    else:
        valid = 0
        break
    if len(s) == len(t) and s!=t:
        valid = 0
        break
print(valid)