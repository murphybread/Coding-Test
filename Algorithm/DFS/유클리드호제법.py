# A,B가 주어 졌을 때(A>B) A를 B로 나눈 후 나머지를 R이라고 하자
# 이 때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다.
# 즉 A -> B , B->R

def gcd(A,B):
    if A % B == 0:
        return B
    else:
        return gcd(B , A%B)


