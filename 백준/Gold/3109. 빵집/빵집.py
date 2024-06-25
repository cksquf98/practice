def Available(row, col):
    return 0 <= row < R and \
           0 <= col < C and \
           roadmap[row][col] == '.'
    

def DFS(row, col):
    global count

    #종료조건 : 마지막 열 도달
    if(col == C-1):
        count += 1
        return True
    
    #현재 방문한 위치 표시
    roadmap[row][col] = 'x'
    
    #왼쪽 위 대각선
    if(Available(row-1, col+1)):
        if(DFS(row-1, col+1)):
            return True
            

    # 직진
    if(Available(row, col+1)):
        if(DFS(row, col+1)):
            return True
        
    # 오른쪽 아래 대각선
    if(Available(row+1, col+1)):
        if(DFS(row+1, col+1)):
            return True


if __name__=="__main__":
    import sys
    input = sys.stdin.readline

    R,C = map(int, input().split())
    roadmap = [[char for char in input().rstrip()] for _ in range(R)]
    count = 0
    
    for i in range(R):
        DFS(i,0)
    print(count)