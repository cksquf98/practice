import sys
input = sys.stdin.readline

row, col = map(int, input().split(' '))
matrix = [list(map(int, input().split(' '))) for _ in range(row)]
result = float('inf')

# 제한조건!! 전에 움직인 방향으로 움직일 수 없다


def DFS(colIndex, direction, currentSum, depth):
    global result
    if depth >= row:
        result = min(result, currentSum)
        return

    if direction != 1 and colIndex - 1 >= 0:
        DFS(colIndex-1, 1, currentSum + matrix[depth][colIndex-1], depth+1)

    if direction != 2:
        DFS(colIndex, 2, currentSum + matrix[depth][colIndex], depth+1)

    if direction != 3 and colIndex + 1 < col:
        DFS(colIndex+1, 3, currentSum + matrix[depth][colIndex+1], depth+1)


for c in range(col):
    DFS(c, 0, 0, 0)

print(result)