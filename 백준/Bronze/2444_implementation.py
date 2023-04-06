n = int(input())

N = 2 * n // 2

for i in range(1, n + 1):
    blank = N - i
    print(blank * " " + (2 * i - 1) * "*")

for i in range(n - 1, 0, -1):
    blank = N - i
    print(blank * " " + (2 * i - 1) * "*")
