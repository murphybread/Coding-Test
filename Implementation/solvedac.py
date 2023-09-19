import sys

input = sys.stdin.readline
n = int(input())


def my_round(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)


if n == 0:
    print(0)
else:
    problem = []
    for _ in range(n):
        problem.append(int(input()))

    cut = my_round(len(problem) * 0.15)
    problem.sort()

    ac = problem[cut : len(problem) - cut]
    print(my_round(sum(ac) / len(ac)))
