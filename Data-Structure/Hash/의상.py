# https://school.programmers.co.kr/learn/courses/30/lessons/42578
from collections import Counter


def solution(clothes):
    answer = 0
    cs = Counter(cloth[1] for cloth in clothes)
    count = 1
    for v in cs.values():
        count = count * (v + 1)
        print(count)

    return count - 1