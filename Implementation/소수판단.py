# 한개의 수에 대한 소수 판별
# 제곱근까지 확인하는 성질
import math


def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
