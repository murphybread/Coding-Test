import sys

input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    word = input().rstrip()
    num = len(word)
    arr.append((word, num))


answer = sorted(set(arr), key=lambda x: (x[1], x))

for i in range(len(answer)):
    print(answer[i][0])
