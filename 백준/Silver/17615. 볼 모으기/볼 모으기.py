import sys
input = sys.stdin.readline

N = int(input())  # 공의 총 개수

ballList = input().rstrip()


def moveBall(index, color, ballList):
    moveCount = 0

    # 0번째랑, 얘네랑 연속된 맨 앞 color 문자열들은 싹 움직일 필요가 없으니까 미리 없애놓자
    ballList = ballList.lstrip(color)
    for i in range(len(ballList)):
        if index != i and ballList[i] == color:
            moveCount += 1
    return moveCount


# 파란공을 왼쪽 끝으로 모아두기
blueLeftCount = moveBall(0, 'B', ballList)

# 파란공을 오른쪽 끝으로 모아두기
blueRightCount = moveBall(0, 'B', ballList[::-1])

# 빨간공을 왼쪽 끝으로 모아두기
redLeftCount = moveBall(0, 'R', ballList)

# 빨간공을 오른쪽 끝으로 모아두기
redRightCount = moveBall(0, 'R', ballList[::-1])


# 이동횟수가 가장 작은 애를 출력
print(min(blueLeftCount, blueRightCount, redLeftCount, redRightCount))