def Available(row, col):
    if((row >= 0 and row < length) and (col >= 0 and col < length) and
       (chesspan[row][col] == False)):
        return True
    else:
        return False
    
def BFS(x, y):
    from collections import deque

    queue = deque()
    queue.append([x,y,0])

    #나이트 이동 위치 큐에 넣어야 함
    while(queue):
        current_x, current_y, cnt = queue.popleft()

        if(current_x == target_x and current_y == target_y):
            return cnt

        chesspan[current_x][current_y] = True

        for row, col in move:
            # print(f"move : ({current_x+row},{current_y+col})")
            if(Available(current_x+row, current_y+col)):
                queue.append([current_x+row, current_y+col, cnt+1])
                chesspan[current_x+row][current_y+col] = True


if __name__=="__main__":
    import sys
    input = sys.stdin.readline

    T = int(input())

    move = [(-1, -2), (-1, 2), (1, -2), (1, 2), 
            (-2, -1), (-2, 1), (2, -1), (2, 1)]

    for _ in range(T):
        length = int(input())
        chesspan = [[False for _ in range(length)] for _ in range(length)]

        loc_x, loc_y = map(int, input().split())
        target_x, target_y = map(int, input().split())

        print(BFS(loc_x,loc_y))