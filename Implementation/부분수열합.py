
# i < partial 원소들 < j
# sum(partial) == k
# len(partialA) len(patialB)
# partial[0] >partial[1]

# 투포인터?로 먼저 answer에 k값을 가지는 부분 수열들 append
# 투포인터 아닌듯. 
# 길이 비교
# 앞쪽 인덱스 비교

#비내림차순 정렬이란? == 오름차순?



def solution(sequence, k):
    answer = []
    
    start = 0
    next = 1
    sub= sequence[0]
    # 부분수열 탐색 중단 조건 index 조건 및 부분 합 조건
    while next < len(sequence):
        sub += sequence[next]
        
        while sub > k:
            sub -= sequence[start]
            start += 1
            
        if sub == k:
            answer.append([start, next])

        
        next+=1

    check_len = answer[0][1]-answer[0][0] +1
    
    for i in range(len(answer)):
        now_len =  answer[i][1]-answer[i][0] +1
        if check_len > now_len:
            check_len = now_len


    last = []

    
    for i in range(len(answer)):
        now_len =  answer[i][1]-answer[i][0] +1
        if now_len == check_len:
            last.append(answer[i])

    last.sort()

    return last[0]