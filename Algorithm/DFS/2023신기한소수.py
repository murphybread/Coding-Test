"""
문제
수빈이가 세상에서 가장 좋아하는 것은 소수이고, 취미는 소수를 가지고 노는 것이다. 요즘 수빈이가 가장 관심있어 하는 소수는 7331이다.

7331은 소수인데, 신기하게도 733도 소수이고, 73도 소수이고, 7도 소수이다. 즉, 왼쪽부터 1자리, 2자리, 3자리, 4자리 수 모두 소수이다! 수빈이는 이런 숫자를 신기한 소수라고 이름 붙였다.

수빈이는 N자리의 숫자 중에서 어떤 수들이 신기한 소수인지 궁금해졌다. N이 주어졌을 때, 수빈이를 위해 N자리 신기한 소수를 모두 찾아보자.

입력
첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다.

출력
N자리 수 중에서 신기한 소수를 오름차순으로 정렬해서 한 줄에 하나씩 출력한다.
"""

# N<= 8인 부분을통해 DFS를 쓸 수 있음을 캐치하기
# 소수라는 속성을 통해 첫 자리수는  2,3,5,7 그 이후 자리수는 짝수를 제외한 1,3,5,7,9 만 고려


# 에라토스테네스의 체로 주어진 n이 소수인지 판별
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N = int(input())

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True



def dfs(number):
    if len(str(number)) == N:
        print(number)
    else:
        for i in range(1,10):
            if i % 2 == 0:
                continue

            # 조건과 이후 실행, dfs 마다 다름
            if is_prime(number*10+i):
                dfs(number*10+i)


# 구현 단계 dfs 마다 다름
dfs(2)
dfs(3)
dfs(5)
dfs(7)

