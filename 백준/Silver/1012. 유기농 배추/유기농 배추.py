def Available(row, col):
    if(0<=row<N and 0<=col<M and graph[row][col] != 0 and visited[row][col] == False):
        return True
    return False


def DFS(row,col):
    #상
    if(Available(row-1,col)):
        visited[row-1][col]=True
        DFS(row-1,col)

    #하
    if(Available(row+1, col)):
        visited[row+1][col]=True
        DFS(row+1, col)

    #좌
    if(Available(row,col-1)):
        visited[row][col-1]=True
        DFS(row,col-1)

    #우
    if(Available(row,col+1)):
        visited[row][col+1]=True
        DFS(row,col+1)


    


if __name__=="__main__":
    import sys
    sys.setrecursionlimit(10000)
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        M,N,K = map(int, input().split())
        graph = [[0]*M for _ in range(N)]
        visited = [[False]*M for _ in range(N)]
        for _ in range(K):
            col, row = map(int,input().split())
            graph[row][col] = 1

        count = 0

        for i in range(N):
            for j in range(M):
                if(Available(i,j)):
                    # print(f"i={i}, j={j}")
                    count+=1
                    DFS(i,j)

        print(count)
        # print(graph)