import sys
input = sys.stdin.readline

N = int(input())  # 공의 총 개수

ballList = input().rstrip()
separateBallList = []


def moveBall(index, color, separateBallList):
    moveCount = 0
    for i in range(len(separateBallList)):
        if index != i and separateBallList[i][0] == color:
            moveCount += len(separateBallList[i])
    return moveCount


ballStr = ''
for ball in ballList:
    if len(ballStr) > 0 and ballStr[0] == ball:
        ballStr += ball
    elif len(ballStr) > 0 and ballStr[0] != ball:
        separateBallList.append(ballStr)
        ballStr = ball
    elif len(ballStr) == 0:
        ballStr += ball
separateBallList.append(ballStr)

# 파란공을 왼쪽 끝으로 모아두기
blueLeftCount = moveBall(0, 'B', separateBallList)

# 파란공을 오른쪽 끝으로 모아두기
blueRightCount = moveBall(len(separateBallList) - 1, 'B', separateBallList)

# 빨간공을 왼쪽 끝으로 모아두기
redLeftCount = moveBall(0, 'R', separateBallList)

# 빨간공을 오른쪽 끝으로 모아두기
redRightCount = moveBall(len(separateBallList) - 1, 'R', separateBallList)


# 이동횟수가 가장 작은 애를 출력
print(min(blueLeftCount, blueRightCount, redLeftCount, redRightCount))