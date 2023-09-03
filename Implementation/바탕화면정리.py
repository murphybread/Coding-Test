# https://school.programmers.co.kr/learn/courses/30/lessons/161990

# 왼쪽 위 끝값 (x최소,y최소), 오른쪽 아래 끝값(x최대,y최대)
# '#'파일위치
# 50개니깐 O(n^2)

def solution(wallpaper):
    answer = []
    col = len(wallpaper[0])
    row = len(wallpaper)

    min_x, min_y = row, col
    max_x, max_y = 0, 0

    for r in range(row):
        for c in range(col):
            if wallpaper[r][c] == '#':
                min_x = min(min_x, r)
                max_x = max(max_x, r + 1)

                min_y = min(min_y, c)
                max_y = max(max_y, c + 1)

        # 만약 해당 #의 x와 y가 left보다 작으면
        # 만약 해당 #의 x와 y가 right보다 크면
    answer.append(min_x)
    answer.append(min_y)
    answer.append(max_x)
    answer.append(max_y)

    return answer