import sys
from collections import deque
input = sys.stdin.readline

N, D = map(int, input().split())

shortcuts = []

distances = [float('inf')] * (D + 1) #inf = 아직 방문하지 않은 위치임을 표시
distances[0] = 0

for _ in range(N):
    start, dest, length = map(int, input().split())
    
    if dest <= D:  # 지름길의 도착 지점이 D 이하인 경우만 고려
        shortcuts.append((start, dest, length))
    


queue = deque([0]) #0번 위치부터 시작
while queue:
    current = queue.popleft()

    #그냥 한 칸 앞으로 이동하는 경우
    if(current+1 <= D and distances[current+1] > distances[current]+1): #방문하지 않은 노드임을 체크
        distances[current+1] = distances[current]+1
        queue.append(current+1)

    #지름길을 사용할 수 있는 경우
    for start, end, length in shortcuts:
        if(start == current and distances[end] > distances[current] + length):
              distances[end] = distances[current] + length
              queue.append(end)

print(distances[D])
