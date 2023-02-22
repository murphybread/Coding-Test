# https://school.programmers.co.kr/learn/courses/30/lessons/42862#
# set을 활용하여 lost와 reserve가 같은 경우 계산할 필요가 없다는걸 고려하였는가?
# sort를 통해 빌려주는 방향에 따라 문제가 생길 수 있는 부분을 고려하였는가?
# 사이즈가 앞뒤만 가능한 부분을 고려하였는가?


def solution(n, lost, reserve):
    answer = 0

    lost_only = list(set(lost) - set(reserve))
    reserver_only = list(set(reserve) - set(lost))

    # 중요한것은 lost_only가 remove되는것
    # 그래서 동작에 문제가 없게하기위해 for문 조건은 reserver_only

    for A in reserver_only:
        # 다음과 같은 경우 테스트 오류
        # n=5 lost[1,3] reserve[2,4] 인 경우
        # 아래와같은 순서면 reserve 2가 lost 3을 없애준후
        # lost 1, reserve 4가 남아 최대값이 안 됨
        # front = A+1
        # back = A-1
        front = A - 1
        back = A + 1

        if front in lost_only:
            lost_only.remove(front)

        elif back in lost_only:
            lost_only.remove(back)

    return n - len(lost_only)
