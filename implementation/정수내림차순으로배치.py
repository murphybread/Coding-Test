https://school.programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    answer = 0
    array= list(str(n))
    R_array = reversed(array)
    R_S_array = sorted ( R_array, reverse=True)
    
    
    return int(''.join(R_S_array))
