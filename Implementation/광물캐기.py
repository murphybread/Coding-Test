# 앞의 5개까지 전달받았을 때 각 곡괭이로 가능한 값 표기 만약 곡괭이 있으면 해당 곡괭이 선택
# 에러사항 만약 그리디 해보자
from typing import List


def solution(picks: List[int], minerals: List[str]) -> int:
    fatigue_values = [{'dia': 1, 'iron': 1, 'stone': 1}, {'dia': 5, 'iron': 1, 'stone': 1},
                      {'dia': 25, 'iron': 5, 'stone': 1}]
    total_fatigue = 0

    for mineral in minerals:
        best_pick = min((pick for pick, count in zip(fatigue_values, picks) if count > 0), key=lambda x: x[mineral])
        total_fatigue += best_pick[mineral]
        picks[fatigue_values.index(best_pick)] -= 1
        if all(count == 0 for count in picks):
            break

    return total_fatigue

