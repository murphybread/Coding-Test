
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
    
    check_len = len(answer[0])
    for i in range(len(answer)):
        if check_len > len(set(answer[i])):
            check_len = len(set(answer[i]))
    
    # 길이 최소값을 구함
    last = []
    check_index = answer[0][0]
    
    for i in range(len(answer)):
        if len(set(answer[i])) == check_len:
            last.append(answer[i])

    last.sort()
    return last[0]