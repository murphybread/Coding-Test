n = 5
data = [10, 20, 30, 40, 50]

m = int(input())

interval_sum = 0
prefix = [0]

for i in data:
    interval_sum += i
    prefix.append(i)


for _ in range(m):
    a, b = map(int, input().split())
    print(prefix[b] - prefix[a - 1])
