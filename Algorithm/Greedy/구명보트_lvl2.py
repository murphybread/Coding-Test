# https://school.programmers.co.kr/learn/courses/30/lessons/42885
# key point
# 1. Greedy Algorithm min + max
# 2. if min +max <= limit
# 3. For efficiecny, use queue structure.

from collections import deque


def solution(people, limit):
    answer = 0

    queue = deque()
    people.sort()
    queue.extend(people)

    while len(queue) > 1:
        M = queue[-1]
        m = queue[0]

        if M + m <= limit:
            queue.popleft()
            queue.pop()
            answer += 1
        else:
            queue.pop()
            answer += 1

    if queue:
        queue.pop()
        answer += 1

    return answer
