# https://school.programmers.co.kr/learn/courses/30/lessons/118667
from collections import deque

# 단순한 생각으로는 sum값을 비교해서 큰놈의 것을 pop,작은놈에 insert후 비교
# 해당 과정 반복
# 이게 n길이가 크고 sum함수라서 시간초과 나는거 같음 60점

# sum이 아니라 +=형태라면? 60점->96.7

# 확인해보는 범위인 for문의 len(q1)을 len(q1)*2에서 len(q1)*3으로 바꾸니 마지막 테스트케이스가 추가됨.
# 뭐지


# 단, 어떤 방법으로도 각 큐의 원소 합을 같게 만들 수 없는 경우, -1을 return 해주세요.
# 큐길이* 2 만큼 돌렸는데도 안되면 -1
def solution(queue1, queue2):
    answer = -2
    q1 = deque(queue1)
    q2 = deque(queue2)

    count = 0
    diff = []

    s1 = sum(q1)
    s2 = sum(q2)

    value = 0
    if (s1 + s2) % 2 != 0:
        return -1

    for _ in range(len(q1) * 3):
        if s1 == s2:
            return count

        elif s1 > s2:
            value = q1.popleft()
            q2.append(value)
            s1 -= value
            s2 += value
            count += 1

        elif s1 < s2:
            value = q2.popleft()
            q1.append(value)
            s2 -= value
            s1 += value
            count += 1

    return -1
