import sys

input = sys.stdin.readline
n = int(input())
stack = [0]
output = []
top = 1

for _ in range(n):
    check = int(input())

    if stack[-1] < check:
        while stack[-1] != check:
            stack.append(top)
            top += 1
            output.append("+")

    if stack[-1] == check:
        stack.pop()
        output.append("-")

    else:
        output.append("-1")
        break

if "-1" in output:
    print("NO")
else:
    for mark in output:
        print(mark)
