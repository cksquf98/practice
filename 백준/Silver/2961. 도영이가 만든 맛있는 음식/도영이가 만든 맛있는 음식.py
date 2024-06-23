#수정사항 반영
# 부분집합 맞는경우 바로 신맛/쓴맛 계산되도록

import sys
input = sys.stdin.readline

N = int(input())

ingredients = []

min_diff = 1000000000

# 재료의 신맛과 쓴맛 입력받기
for _ in range(N):
    S, B = map(int, input().split())
    ingredients.append((S, B))

# 부분집합을 생성하여 신맛과 쓴맛의 차이를 계산하는 함수
def findMin():
    global min_diff
    # 1부터 2^N-1 까지의 수로 부분집합을 표현 (공집합 제외)
    for subset_mask in range(1, 1 << N):
        total_sour = 1
        total_bitter = 0
        for i in range(N):
            if subset_mask & (1 << i):  # i번째 재료가 부분집합에 포함되는 경우
                total_sour *= ingredients[i][0]
                total_bitter += ingredients[i][1]
        min_diff = min(min_diff,abs(total_sour - total_bitter))

# 최소 차이를 찾는 함수 호출
findMin()

# 결과 출력
print(min_diff)