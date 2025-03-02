# 이 문제 또 못풀겠다 아놔,,, 어렵다!!!

import sys
from collections import deque
input = sys.stdin.readline

N, D = map(int, input().split(" "))  # 지름길 개수, 도착 지점
fastRoad = []

for _ in range(N):
    roadInput = list(map(int, input().split(" ")))  # [출발 위치, 도착 위치, 소요거리]

    if roadInput[1] <= D and roadInput[1] - roadInput[0] > roadInput[2]:
        fastRoad.append(roadInput)

# D까지의 모든 거리 하나하나를 비교하면서 거리를 계산해줘야 함
distance = [float('inf') for _ in range(D+2)] # D+1까지 공간이 필요하기 때문에!!!
distance[0] = 0

queue = deque([0])  # 0번째부터 출발
while queue:
    current = queue.popleft()

    # 한 칸 앞으로 이동하는 경우 -> 지름길보다 하나 더 가는게 빠른 경우 갱신 필요
    if current <= D and distance[current] + 1 < distance[current + 1]:
        distance[current + 1] = distance[current] + 1
        queue.append(current+1)

    # 지름길을 갈 수 있는 경우
    for start, end, extraDistance in fastRoad:
        if start == current and distance[end] > distance[current] + extraDistance:
            distance[end] = distance[current] + extraDistance
            queue.append(end)

print(distance[D])
