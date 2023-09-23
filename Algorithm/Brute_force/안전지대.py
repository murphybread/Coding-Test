# https://school.programmers.co.kr/learn/courses/30/lessons/120866

# 구현 n작으니 모든 경우에 대해 2차원 배열을 2로 만들기


def solution(board):
    answer = 0
    unsafe = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for us in unsafe:
                    dx = i + us[0]
                    dy = j + us[1]

                    if 0 <= dx < n and 0 <= dy < n and board[dx][dy] != 1:
                        board[dx][dy] = 2

    for line in board:
        for b in line:
            if b == 0:
                answer += 1

    return answer
