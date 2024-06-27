#인접한 노드를 따라서 끝까지 쭉 가는게 아니고
#인접 노드들 확산 -> 그 노드들의 인접 노드들 확산 -> ...
#BFS!!!

def Available(row, col):
    if(row < 0 or row >= R):
        return False
    
    if(col < 0 or col >= C):
        return False
    
    if(tomatoes[row][col] == -1 or tomatoes[row][col] == 1 or visited[row][col] == True):
        return False

    return True


def BFS():
    day = 0
    queue = deque()

    # BFS함수 내에서 토마토 찾아서 좌표를 큐에 넣어야 함
    for i in range(R):
        for j in range(C):
            if(tomatoes[i][j] == 1):
                queue.append([i,j,0]) # 세번째 인자가 날짜임!! 
                visited[i][j] = True


    #BFS 순회
    while(len(queue) > 0):
        current_loc = queue.popleft()
        
        r = current_loc[0]
        c = current_loc[1]
        day = current_loc[2]

        #상
        if(Available(r+1,c)):
            queue.append([r+1, c, day+1])
            visited[r+1][c] = True
            #익은 토마토로 변경
            tomatoes[r+1][c] = 1
        
        #하
        if(Available(r-1,c)):
            queue.append([r-1, c, day+1])
            visited[r-1][c] = True
            #익은 토마토로 변경
            tomatoes[r-1][c] = 1

        #좌
        if(Available(r,c-1)):
            queue.append([r, c-1, day+1])
            visited[r][c-1] = True
            #익은 토마토로 변경
            tomatoes[r][c-1] = 1

        #우
        if(Available(r,c+1)):
            queue.append([r, c+1, day+1])
            visited[r][c+1] = True
            #익은 토마토로 변경
            tomatoes[r][c+1] = 1

    #토마토 확인
    for tomato_line in tomatoes:
        if 0 in tomato_line:
            return -1
        
    return day




if __name__=="__main__":
    import sys
    from collections import deque
    input = sys.stdin.readline

    C, R = map(int, input().split())

    tomatoes = [list(map(int,input().split())) for _ in range(R)]
    visited = [[False for _ in range(C)] for _ in range(R)]

    print(BFS())