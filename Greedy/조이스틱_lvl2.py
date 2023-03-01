# https://school.programmers.co.kr/learn/courses/30/lessons/42860
# 출처 https://velog.io/@jqdjhy/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1-Greedy

# 위아래 횟수
# 좌우 횟수
# 좌우 기준은 연속된 A의개수와 A의 위치에따라 정방향,역방향 선택

def solution(name):
    answer = 0
    
    min_move = len(name) - 1
    
    for i, char in enumerate(name):
    	# 해당 알파벳 변경 최솟값 추가
        
        # min(알파벳이 A에 가까운 경우, 알파벳이 Z에 가까운 경우)
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        # i는연속된 A시작, next는 연속된 A의 끝
        next = i + 1
        # A인 문자인경우 and next가 name글자 수 범위 이내인경우
        
        
        while next < len(name) and name[next] == 'A':
            next += 1
        
        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        min_move = min([min_move, 2 *i + len(name) - next, i + 2 * (len(name) -next)])
            
        
        
    answer += min_move
    return answer