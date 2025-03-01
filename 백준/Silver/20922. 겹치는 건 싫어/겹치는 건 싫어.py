import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N, K = map(int, input().split(" "))  # N: 수열 전체 길이, K: 겹치는거 허용 갯수
numList = list(map(int, input().split(" ")))

count = defaultdict(int)
length = 0

# 지선생의 힌트 : 슬라이딩 윈도우
slide = deque([])
for num in numList:
    count[num] += 1
    slide.append(num)

    if count[num] > K:
        while True:
            popNum = slide.popleft()
            count[popNum] -= 1
            if popNum == num:
                break

    if length < len(slide):
        length = len(slide)

if length < len(slide):
    length = len(slide)

print(length)