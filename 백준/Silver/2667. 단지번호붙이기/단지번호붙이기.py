def Available(row, col):
    if((row >= 0 and row < N) and (col >= 0 and col < N)
       and (not visited[row][col]) and (graph[row][col] == "1")):
        return True
    
    else:
	    return False


def BFS(r, c):
    queue = deque()
	
    queue.append([r, c])
    visited[r][c] = True
    count = 1
	
    while queue:
        row, col = queue.popleft()
        # print(f"row={row}, col = {col}")

        #상
        if(Available(row-1, col)):
            #  print("top")
             queue.append([row-1, col])
             visited[row-1][col] = True
             count += 1

        #하
        if(Available(row+1, col)):
            #  print("bottom")
             queue.append([row+1, col])
             visited[row+1][col] = True
             count += 1

        #좌
        if(Available(row, col-1)):
            #  print("left")
             queue.append([row, col-1])
             visited[row][col-1] = True
             count += 1

        #우
        if(Available(row, col+1)):
            #  print("right")
             queue.append([row, col+1])
             visited[row][col+1] = True
             count += 1        

    return count



import sys
from collections import deque
	
input = sys.stdin.readline
N = int(input())

graph = [list(map(str,input().rstrip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
     
apt = deque()
for row in range(N):
    for col in range(N):
        if(graph[row][col] == "1" and not visited[row][col]): 
        #    print(f"node = ({row},{col})")
           apt.append(BFS(row, col))


print(len(apt))
for num in sorted(apt):
     print(num)