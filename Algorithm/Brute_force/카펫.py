# https://school.programmers.co.kr/learn/courses/30/lessons/42842

# 수식 세우기
# 특정 조건을 만족하는 x,y찾기

# 넓이 = x *y , x>=y ,5000 and 2,000,000
# 노랑 = (x-2) * (y-2)
# 갈색은 2x+2y = 2(x+y) -4
# 식  xy = xy -2(x+y) +4 + 2(x+y) -4
# xy = yellow + brown
# x = (yellow+brown)/y

# 마지막 검증: xy가여러 쌍이 나올 수 있는데 이 때 brown = 2(x+y) -4를 검증

def solution(brown, yellow):
    answer = []

    for i in range(1, brown):
        y = (brown + yellow) // i
        if i >= y and (2 * (i + y) - 4) == brown:
            return [i, y]

