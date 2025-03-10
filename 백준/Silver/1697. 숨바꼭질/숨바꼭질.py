import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split(" "))

# 재귀로 풀어볼까....했지만 !!! 리컬젼 에러가 자꾸 나서 지선생에게 도움을 받아보았다
# 최단거리, 최적해 보장이 되는 BFS를 사용해야한다고 알려줬다


def BFS(current, k, time):
    queue = deque([(current, time)])  # 현재 위치, time
    visited = {}

    while queue:
        location, currentTime = queue.popleft()

        # 종료 조건
        if location == k:
            print(currentTime)
            break

        if location in visited:
            continue

        visited[location] = True

        # 순간이동
        if location * 2 <= 100000 and (location * 2) not in visited:
            queue.append((location * 2, currentTime + 1))

        # 뒤로 -1칸
        if location - 1 >= 0 and (location - 1) not in visited:
            queue.append((location - 1, currentTime + 1))

        # 앞으로 +1칸
        if location + 1 <= 100000 and (location + 1) not in visited:
            queue.append((location + 1, currentTime+1))


BFS(N, K, 0)