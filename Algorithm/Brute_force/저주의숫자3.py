# https://school.programmers.co.kr/learn/courses/30/lessons/120871?language=python3

# def solution(n):
#     answer = []
#     count = 0
#     # n은 100이라 전부 구해놓기
#     i = 1
#     while len(answer) < n:
#         sr = str(i)
#         if '3'in sr or (i+count)%3==0:
#             count+=1
#             continue
            
#         answer.append(i+count)
#         print(i,count,answer)
#         i+=1
    
#     return answer

def solution(n):
    answer = []
    num = 1
    while len(answer) < n:
        
        if '3' in str(num) or num % 3 == 0:
            num += 1
            continue
        answer.append(num)
        num += 1
    
    return answer[-1]
