# 판 두 개 만들어놓고, 이중 for문으로 비교후 가장 작은 값
m, n = map(int, input().split())

plate1 = []
plate2 = []

for i in range(1, 9):
    if i % 2 == 1:
        plate1.append(["B", "W", "B", "W", "B", "W", "B", "W"])
        plate2.append(["W", "B", "W", "B", "W", "B", "W", "B"])
    else:
        plate2.append(["B", "W", "B", "W", "B", "W", "B", "W"])
        plate1.append(["W", "B", "W", "B", "W", "B", "W", "B"])


plate = []
for i in range(m):
    line = list(input())
    plate.append(line)

min_changes = 64

for i in range(m - 7):
    for j in range(n - 7):
        change1 = 0
        change2 = 0
        for x in range(8):
            for y in range(8):
                if plate[i + x][j + y] != plate1[x][y]:
                    change1 += 1
                if plate[i + x][j + y] != plate2[x][y]:
                    change2 += 1
        min_changes = min(min_changes, change1, change2)

print(min_changes)

#    test_plate
