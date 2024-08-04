def is_available(row, col, dochi):
    if(row >= 0 and row < R) and (col >= 0 and col < C):
        if(dochi):
            if(not visited[row][col]):
                return forest[row][col] not in ["*", "X"]
        else:
            return (forest[row][col] == ".")
    
    return False

def BFS():
    from collections import deque

    #물 큐
    water = deque()
    #고슴도치 큐
    dochi = deque()

    #물이랑 고슴도치 위치 찾아야 해
    for i in range(R):
        for j in range(C):
            if(forest[i][j] == "*"):
                water.append((i,j))

            elif(forest[i][j] == "S"):
                dochi.append((i,j,0))
                visited[i][j]=True # 고슴도치 시작 위치 방문 처리


    while dochi:
        
        #물 침투
        for _ in range(len(water)):
            water_x, water_y = water.popleft()

            #상
            if(is_available(water_x-1, water_y, False)):
                water.append((water_x-1, water_y))
                forest[water_x-1][water_y] = "*"

            #하
            if(is_available(water_x+1, water_y, False)):
                water.append((water_x+1, water_y))
                forest[water_x+1][water_y] = "*"

            #좌
            if(is_available(water_x, water_y-1, False)):
                water.append((water_x, water_y-1))
                forest[water_x][water_y-1] = "*"

            #우
            if(is_available(water_x, water_y+1, False)):
                water.append((water_x, water_y+1))
                forest[water_x][water_y+1] = "*"


        #고슴도치 이동
        for _ in range(len(dochi)):
            dochi_x, dochi_y, cnt = dochi.popleft()

            if(forest[dochi_x][dochi_y] == "D"):
                return cnt
    


            #상
            if(is_available(dochi_x-1, dochi_y, True)):
                dochi.append((dochi_x-1, dochi_y,cnt+1))
                visited[dochi_x-1][dochi_y] = True

            #하
            if(is_available(dochi_x+1, dochi_y, True)):
                dochi.append((dochi_x+1, dochi_y, cnt+1))
                visited[dochi_x+1][dochi_y] = True

            #좌
            if(is_available(dochi_x, dochi_y-1, True)):
                dochi.append((dochi_x, dochi_y-1, cnt+1))
                visited[dochi_x][dochi_y-1] = True

            #우
            if(is_available(dochi_x, dochi_y+1, True)):
                dochi.append((dochi_x, dochi_y+1, cnt+1))
                visited[dochi_x][dochi_y+1] = True

        # print(forest)
        # print(f"visited : {visited}")
    
        
    return "KAKTUS"

if __name__=="__main__":
    import sys
    input = sys.stdin.readline
    R, C = map(int, input().split())

    forest = [list(map(str, input().rstrip())) for _ in range(R)]
    visited = [[False] * C for _ in range(R)]
    print(BFS())