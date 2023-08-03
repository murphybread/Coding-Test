# https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    """
    연속된 수들로 특정 값 비교 -> 투 포인터

    start = for문 , end =1
    
    연속된 수들의 합 < n and end <=n
    연속된 수들의 값 == n
    연속된 수들의 값 -= start
    
    """
    answer = 0
    
    internal_sum =  0
    end = 1
    
    for start in range(1, n+1):
        while internal_sum < n and end <=n:
            internal_sum +=end
            end+=1
            
        if internal_sum == n:
            answer +=1
        internal_sum -= start
    
    return answer
