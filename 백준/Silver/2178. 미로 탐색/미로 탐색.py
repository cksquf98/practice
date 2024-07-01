def Available(row, col):
    if(0 <= row < N and 0 <= col < M and \
       visited[row][col]==False and miro[row][col]==1):
        return True
    
    return False

def BFS():
    # visited = [] 이걸로 in 연산하니까 시간 대박 오래걸림;
    visited[0][0] = True
    # queue = [[0,0,1]] #세번째 인자가 move 횟수
    #queue: 리스트 대신 deque를 써야함 아놔 -> pop(0)연산이 O(n)이여서
    queue = deque([[0,0,1]])


    while queue:
        # position = queue.pop(0)
        position = queue.popleft() # <<< O(1)시간복잡도 >>>
        row = position[0]
        col = position[1]
        cnt = position[2]

        if(row == N-1 and col == M-1):
            return cnt
        
        #상
        if(Available(row-1, col)):
            queue.append([row-1, col, cnt+1])
            visited[row-1][col] = True
                

        #하
        if(Available(row+1, col)):
            queue.append([row+1, col, cnt+1])
            visited[row+1][col] = True

        #좌
        if(Available(row, col-1)):
            queue.append([row, col-1, cnt+1])
            visited[row][col-1] = True

        #우
        if(Available(row, col+1)):
            queue.append([row, col+1, cnt+1])
            visited[row][col+1] = True
        

        # print(visited)
        # print()
        # print(queue)
        # print("=======================")



if __name__=="__main__":
    #(1, 1)에서 출발 -> 최단경로!!! ** BFS
    #칸을 셀 때에는 시작 위치와 도착 위치도 포함
    from collections import deque
    import sys
    input = sys.stdin.readline

    N,M = map(int,input().split())
    miro = [[int(char) for char in input().rstrip()] for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    
    print(BFS())