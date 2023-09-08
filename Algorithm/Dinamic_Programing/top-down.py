import time
# 한 번 계싼된 결과를 메모이제이션하기 위한 배열
d = [0] * 100

start = (time.time())
# 피보나치를 탑다운 방식으로 구현
def fibo(n):
    # 재귀가 끝나는 조건 명시
    if n ==1 or n== 2:
        return 1
    if d[n] !=0 :
        return d[n]

    d[n] = fibo(n-1) + fibo(n-2)
    return d[n]

print(fibo(99))

end = (time.time())

print(end-start)