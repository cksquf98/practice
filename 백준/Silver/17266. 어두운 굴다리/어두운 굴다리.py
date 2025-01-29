import sys
import math
input = sys.stdin.readline


N = int(input())  # 굴다리의 길이
M = int(input())  # 가로등의 개수
position = list(map(int, input().split(' ')))  # 가로등 설치 위치

minLength = 0  # 마지막에 2 곱해서 총 길이로 출력해야겠다

if M > 1:
    for i in range(M):
        currentLength = 0
        # 맨 처음 위치
        if i == 0:
            currentLength = max(position[i], math.ceil(
                (position[i+1] - position[i]) / 2))
        # 맨 마지막 위치
        elif i == M-1:
            currentLength = max(
                math.ceil((position[i] - position[i-1]) / 2), N - position[i])
        else:
            currentLength = max(math.ceil(
                (position[i+1] - position[i]) / 2), math.ceil((position[i] - position[i-1]) / 2))

        if minLength < currentLength:
            minLength = currentLength

else:
    minLength = max(position[0], N - position[0])

print(minLength)
