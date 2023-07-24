import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int,input().split()))
# prefix_sum =[] 틀린 경우. index를 편집하지 않기위해 index번호와 배열의 위치를 일치시키기 위해 0번째 원소 선언
prefix_sum =[0]
temp = 0


for i in numbers:
    temp = temp +i
    prefix_sum.append(temp)
    
for _ in range(M):
    s,e = map(int,input().split())
    print(prefix_sum[e] - prefix_sum[s-1])
    

