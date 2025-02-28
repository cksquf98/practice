import sys
from collections import deque
input = sys.stdin.readline

rowNum, colNum = map(int, input().split(" "))
roadMap = []
distance = [[-1 for _ in range(colNum)] for _ in range(rowNum)]


def availableMove(roadMap, row, col):
    global distance
    if (0 <= row < rowNum) and (0 <= col < colNum) and roadMap[row][col] != 0 and distance[row][col] == -1:
        return True
    return False


def calculateDistance(roadMap, distance, row, col):
    queue = deque([[row, col, 0]])  # 세번째가 거리를 나타내는 수
    distance[row][col] = 0

    while queue:
        location_r, location_c, depth = queue.popleft()

        # 상
        if availableMove(roadMap, location_r-1, location_c):
            queue.append([location_r-1, location_c, depth+1])
            distance[location_r-1][location_c] = depth+1

        # 하
        if availableMove(roadMap, location_r+1, location_c):
            queue.append([location_r+1, location_c, depth+1])
            distance[location_r+1][location_c] = depth+1

        # 좌
        if availableMove(roadMap, location_r, location_c-1):
            queue.append([location_r, location_c-1, depth+1])
            distance[location_r][location_c-1] = depth+1

        # 우
        if availableMove(roadMap, location_r, location_c+1):
            queue.append([location_r, location_c+1, depth+1])
            distance[location_r][location_c+1] = depth+1
    return distance


for i in range(rowNum):
    roadMap.append(list(map(int, input().split(" "))))

for i in range(rowNum):
    for j in range(colNum):
        if roadMap[i][j] == 0:
            distance[i][j] = 0
        if roadMap[i][j] == 2:
            distance = calculateDistance(roadMap, distance, i, j)


for colList in distance:
    for col in colList:
        print(col, end=' ')
    print()