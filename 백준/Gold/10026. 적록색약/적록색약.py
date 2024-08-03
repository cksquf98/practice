def Available(row, col, color, normalPerson):
    #행렬 인덱스 체크
    if(row >= 0 and row < N) and (col >= 0 and col < N):
        #일반인
        if(normalPerson):
            #방문 안한 곳(False) + 동일한 색깔인지 체크
            return not visited[row][col] and (color == pic[row][col])

        #적록
        else:
            #방문 안한 곳(True) + 동일한 색깔인지 체크(빨강 초록 체크부분 추가)
            return (visited[row][col]) and (color == pic[row][col] or (color in "RG" and pic[row][col] in "RG"))
    return False    



def BFS(normalPerson):
    from collections import deque

    ans = 0
    for row in range(N):
        for col in range(N):
            if(visited[row][col] != normalPerson):
                queue = deque()
                color = pic[row][col]
                queue.append([row, col])
                ans += 1
                while queue:
                    x, y = queue.popleft()

                    #일반인은 방문 시 False -> True, 적록은 True -> False로 바뀌도록
                    visited[x][y] = normalPerson

                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if Available(nx, ny, color, normalPerson):
                            queue.append((nx, ny))
                            visited[nx][ny] = normalPerson

                
                
    print(ans, end = ' ')


import sys
input = sys.stdin.readline

N = int(input())

pic = [list(map(str,input().rstrip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

#일반인
BFS(True)

#적록색약 체크하기 전에 pic에 있는 G를 R로 바꿔버리깅
for i in range(N):
    for j in range(N):
        if(pic[i][j] == "G"):
            pic[i][j] = "R"

BFS(False)