# https://school.programmers.co.kr/learn/courses/30/lessons/42883
# 출처 https://wellsw.tistory.com/m/205

#시간초과 문제를 해결하기위한 스택 구조 O(n)
def solution(number, k):
    stack = []
    
    for n in number:
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)

    # 아직 제거되지 못 한 숫자를 뒤에서 삭제
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)