
def solution(name):
    answer = 0
    

    # 연속된 A의 개수와 위치에 따라 정방향 및 역방향 위치 고려
    # 연속된 A의 개수 - 떨어진 위치가 큰 쪽으로 방향 선택
    forward = 0
    backward = 0
    for i in range(len(name)):
        
        if name[i] == 'A':
            forward +=1
            start = i
        else:
            forward = 0
            
        if name[-(i+1)] == 'A':
            backward += 1
            start_b = (len(name) - 1) - i
            
    
    print(forward, backward)
    
        
    for n in name:
            
        c = ord(n)
        answer+=1
        if c == 65:
            continue
        if c <77:
            answer += c-65
            
        else:
            answer += 90-c+1
            #print(c,chr(c),answer)
        
        
    answer-=1
    return answer


