https://school.programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    answer = []
    # a*b= G*L , a>b
    if n > m:
        a = n
        b = m
    else:
        a = m
        b = n
    
    #gcd
    
    r = a%b
    while r!=0:
        a = b
        b = r
        r = a%b
        
    gcd = b
    answer.append(gcd)
    
    #lcm
    lcm = int((n*m) /gcd)
    answer.append(lcm)
    return answer
