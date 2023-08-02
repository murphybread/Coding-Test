"""Two pointer

    Two pointer의 겨우 두개의 포인터를 어떻게 세울 것인가, 어떤기 준으로 움직일 것인가가 중요
    
    # 오름차순 정령
    # 두개 값을 이용 
    # i,j > M  j--
    # i,j < M  i++
    # i,j = M count ++, i++,j--

    # if if if와 if elif elif의 차이점은 위의 두 if문에 의해 i와 j가 바뀌면서 3번째 count if문이 예기치 않게 동작할 수 있기 때문
"""

import sys
input = sys.stdin.readline

N =int(input())
M =int(input())
armors  = list(map(int, input().split()))
armors.sort()

count = 0
i = 0
j = len(armors) - 1

while i < j:
    if armors[i] + armors[j] > M:
        j  -= 1
    elif armors[i] + armors[j] < M:
        i +=1
    elif armors[i] + armors[j] == M:
        count +=1
        i +=1
        j -=1




print(count)



