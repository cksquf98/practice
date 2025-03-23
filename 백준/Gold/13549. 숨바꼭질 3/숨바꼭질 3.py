import sys
from collections import deque
input = sys.stdin.readline

# 전에 BFS로 풀라고 했던 문제다 근데 순간이동이 0초로 줄었넹
N, K = map(int, input().split(" "))
visited = {}

def BFS(current, k, time):
    queue = deque([(current, time)])

    while queue:
        currentLoc, time = queue.popleft()

        if currentLoc == k:
            print(time)
            break

        if currentLoc in visited:
            continue

        visited[currentLoc] = True

        # 순간 이동
        if currentLoc * 2 <= 100000 and currentLoc*2 not in visited:
            queue.append((currentLoc*2, time))

        # 한 칸 이동
        if currentLoc - 1 >= 0 and currentLoc-1 not in visited:
            queue.append((currentLoc-1, time+1))

        if currentLoc + 1 <= 100000 and currentLoc+1 not in visited:
            queue.append((currentLoc+1, time+1))

BFS(N, K, 0)