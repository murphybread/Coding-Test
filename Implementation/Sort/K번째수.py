# https://school.programmers.co.kr/learn/courses/30/lessons/42748


def solution(array, commands):
    answer = []
    
    # 2차원 배열에서 각 원소는 1차원배열
    for part in commands:
        
        
        # i부터 j까지의 부분집합
        
        i,j,k = part[0], part[1], part[2]
        partial = array[i-1:j]
        
        # 정렬
        partial.sort()
        
        
        # 해당 부분집합에서k 번째
        answer.append(partial[k-1])
        
    
    
    
    return answer