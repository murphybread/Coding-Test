import math

count = 0
S = input()

for s in S:
    num = ord(s)
    if num >= 87:
        num = 9
        pass
    elif num >= 80 and num <= 83:
        num = 7
        pass
    elif num == 86:
        num = 8
        pass
    else:
        num = math.ceil((num % 64) / 3) + 1
    
    count += num + 1
print(count)
