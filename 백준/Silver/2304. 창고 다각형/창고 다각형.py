import sys
from collections import deque
input = sys.stdin.readline

N = int(input())  # 기둥 개수
pillarList = []
flag = False


maxPillar = [0, 0]
for _ in range(N):
    inputPillar = list(map(int, input().split(' ')))
    if inputPillar[1] > maxPillar[1]:
        maxPillar = inputPillar
    pillarList.append(inputPillar)
pillarList.sort(key=lambda x: x[0])
pillarList = deque(pillarList)


area = 0
currentMaxPillar = [0, 0]
while pillarList:
    pillar = pillarList.popleft()
    if pillar == maxPillar:
        area += (pillar[0] - currentMaxPillar[0]) * currentMaxPillar[1]
        # 이 기둥 면적 더하기
        area += pillar[1]
        currentMaxPillar = [0, 0]
        break
    elif pillar[1] > currentMaxPillar[1]:
        # 면적 계산
        area += (pillar[0] - currentMaxPillar[0]) * currentMaxPillar[1]
        currentMaxPillar = pillar
    else:  # 더 낮은 기둥이 사이에 껴있는 경우
        continue

# maxPillar를 만나면 == 나보다 더 큰 애가 없는 경우 -> 거꾸로 면적을 계산하면서 더하는 함수를 만들어서 실행시키도록 하잣
while pillarList:
    pillar = pillarList.pop()
    if pillar[1] > currentMaxPillar[1]:
        # 면적 계산
        area += (currentMaxPillar[0] - pillar[0]) * currentMaxPillar[1]
        currentMaxPillar = pillar
    else:
        continue

# currentPillar랑 maxPillar 사이 면적 확인
area += (currentMaxPillar[0] - maxPillar[0]) * currentMaxPillar[1]

print(area)