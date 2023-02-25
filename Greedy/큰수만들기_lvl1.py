# https://school.programmers.co.kr/learn/courses/30/lessons/42883
# 출처 https://wellsw.tistory.com/m/205


# 시간초과 문제를 해결하기위한 스택 구조 O(n)
def solution(number, k):
    stack = []

    for n in number:

        #가장 최근에 push한 숫자보다 낮은 경우 pop 
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)

    
    # 아직 제거되지 못 한 숫자를 뒤에서 삭제
    # 예를 들어 91995,3 인경우 for문을 빠져나온뒤 9995 k=2 이기에 앞의 99까지만 출력
    if k > 0:
        stack = stack[:-k]

    return "".join(stack)
