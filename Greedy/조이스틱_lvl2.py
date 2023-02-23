def solution(name):
    answer = 0
    print(ord('A'), ord('Z'))
    
    

    for n in name:
        c = ord(n)
        if c <77:
            answer += c-65
            print(c,chr(c),answer)
        else:
            answer += 90-c+1
            print(c,chr(c),answer)
        #print(c,answer)
        answer+=1
    answer-=1
    return answer