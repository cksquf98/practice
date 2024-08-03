def Available(row, col, color, rgPerson):
    if(row >= 0 and row < N) and (col >= 0 and col < N):
        if(rgPerson):
            return (visited[row][col] == False) and (color == pic[row][col])
            

        else:
            return (visited[row][col] == True) and (color == pic[row][col])
    return False


def BFS(rgPerson=True):
    from collections import deque


    
    count = 0
    for row in range(N):
        for col in range(N):
            if(visited[row][col] != rgPerson):
                queue = deque()
                queue.append([row, col])
                color = pic[row][col]
                count += 1
                while queue:
                    x, y = queue.popleft()
                    visited[x][y] = rgPerson

                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if Available(nx, ny, color, rgPerson):
                            queue.append((nx, ny))
                            visited[nx][ny] = rgPerson
                
    print(count, end = ' ')


import sys
input = sys.stdin.readline

N = int(input())

pic = [list(map(str,input().rstrip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

#일반인
BFS(True)

#적록색약
for i in range(N):
    for j in range(N):
        if(pic[i][j] == "G"):
            pic[i][j] = "R"

BFS(False)