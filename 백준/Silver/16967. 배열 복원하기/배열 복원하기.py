import sys
from collections import deque
input = sys.stdin.readline

H, W, X, Y = map(int, input().split(' '))

arr = [list(map(int, input().split(' '))) for _ in range(H+X)]


for i in range(H):
    for j in range(W):
        me = arr[i][j]
        target = arr[i+X][j+Y]

        arr[i+X][j+Y] = target - me

for i in range(H):
    for j in range(W):
        print(arr[i][j], end=' ')
    print()