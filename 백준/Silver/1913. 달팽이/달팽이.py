import sys
# import math

input = sys.stdin.readline


N = int(input())
num = int(input())

arr = [[0 for _ in range(N)] for _ in range(N)]

arr[N//2][N//2] = 1

s_num = N*N

for depth in range(N//2):

    #left
    for j in range(depth, N-depth):
        arr[j][depth] = s_num
        s_num -= 1

    #bottom
    for j in range(depth+1,N-depth-1):
        arr[N-depth-1][j] = s_num
        s_num -= 1

    #right
    for j in range(depth,N-depth):
        arr[N-j-1][N-depth-1] = s_num
        s_num -= 1

    #top
    for j in range(depth+1,N-depth-1):
        arr[depth][N-j-1] = s_num
        s_num -= 1

num_row = 0
num_col = 0

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
        if(arr[i][j] == num):
            num_row = i+1
            num_col = j+1
    print()

print(f"{num_row} {num_col}")