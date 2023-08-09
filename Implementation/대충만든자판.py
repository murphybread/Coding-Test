# https://school.programmers.co.kr/learn/courses/30/lessons/160586

def solution(keymap, targets):
    answer = []
    
    for word in targets:
        number = 0
        for w in word:
            num = []
            for key in keymap:
                if w in key:
                    num.append(key.index(w))
            if len(num) == 0:
                # return [-1]
                number=-1
                break
            
            number+= min(num)+1
        answer.append(number)
    return answer
