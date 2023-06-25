import itertools


N, M = map(int, input().split())  
cards = list(map(int,input().split()))
check = 0


combi = itertools.combinations(cards, 3)
for c in combi:
    test = sum(c)
    if test <= M and test >= check:
        check = test

print(check)
        