import sys
from collections import deque
input = sys.stdin.readline

N = int(input())  # 총 사람 수
line = [N for _ in range(N)]
leftPersonNum = list(map(int, input().split(" ")))

def findSeat(line, num, leftNum):
    count = 0
    index = 0

    while index < N:
        if line[index] == N and count == leftNum:
            return index
        if line[index] > num:
            count += 1
        index += 1
    return -1

for i in range(N-1):
    num = i+1
    leftNum = leftPersonNum[i]
    seatIndex = findSeat(line, num, leftNum)
    if seatIndex != -1:
        line[seatIndex] = num

for elem in line:
    print(elem, end=' ')