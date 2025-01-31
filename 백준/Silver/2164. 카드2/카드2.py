from collections import deque
import sys
input = sys.stdin.readline

totalCard = int(input())

cardList = deque([number for number in range(1, totalCard+1)])

while len(cardList) > 1:
    cardList.popleft()
    moveCard = cardList.popleft()
    cardList.append(moveCard)

print(cardList.popleft())
