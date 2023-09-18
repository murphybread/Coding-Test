import sys

input = sys.stdin.readline
n = int(input())

if n == 0:
    print(0)
else:
    problem = []
    for _ in range(n):
        problem.append(int(input()))
    print(problem)

    cut = round(len(problem) * 0.15)
    problem.sort()

    ac = problem[cut : len(problem) - cut]

    if len(ac) == 0:
        print(0)
    else:
        print(round(sum(ac) / len(ac)))
