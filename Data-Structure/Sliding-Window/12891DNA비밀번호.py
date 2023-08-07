# main point
# O(N) 고려하기 위해 원소 추가,삭제 시간복잡도 고려
# counter if문 고려

from collections import Counter

S, P = map(int, input().split())
DNA = input().strip()
DNA_A, DNA_C, DNA_G, DNA_T = map(int, input().split())

condition = Counter({"A": DNA_A, "C": DNA_C, "G": DNA_G, "T": DNA_T})

# 첫 윈도우
rolling_counter = Counter(DNA[:P])
count = 0


# 모든 요소를 비교하여 만약 모든요소 값이 more than 이라면 True 반환
if rolling_counter >= condition:
    count += 1

# Slide the window
for i in range(S-P+1):
    # 한칸 이동하며 start위치 만큼 값 감소
    rolling_counter[DNA[i]] -= 1
    
    # end 예외 설정
    # 한칸 이동하며 end위치 만큼 값 증가
    if P+i >= S:
        continue
    else:
        rolling_counter[DNA[P+i]] += 1

    # Check the current window
    if rolling_counter >= condition :
        count += 1

print(count)
