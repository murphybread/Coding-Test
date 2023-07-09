# https://school.programmers.co.kr/learn/courses/30/lessons/159994

def solution(cards1, cards2, goal):
    k, i, j = 0, 0, 0

    while k < len(goal):
        if i < len(cards1) and goal[k] == cards1[i]:
            k += 1
            i += 1
        elif j < len(cards2) and goal[k] == cards2[j]:
            k += 1
            j += 1
        else:
            return "No"
    
    return "Yes" if i + j == len(goal) else "No"
