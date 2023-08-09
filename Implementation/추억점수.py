# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    """
    
    name = []
    yearning = []
    photo = []
    
    1. name값과 yearning값을 딕셔너리로 묶기
    2. zip 함수와 dict함수 활용
    3. photo에서 각 원소의 value를 찾아서 더해주기
    
    """
    answer = []
    score = 0
    score_set = dict(zip(name, yearning))

    for peoples in photo:
        for people in peoples:
            if people in score_set:
                score += score_set[people]
        answer.append(score)
        score = 0

    return answer

# zip함수 활용하기
# zip함수와 dict연결하기
# 키가 없는 dict에 대한 deny값 처리하기