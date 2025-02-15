import sys
input = sys.stdin.readline

categoryNum, M = map(int, input().split(' '))  # 분류 수, 입력 수

category = []


def findPartition(limit, start, destination, category):
    if destination <= start:
        global done
        done[limit] = category[start][0]
        print(category[start][0])
        return

    middleIndex = (destination + start) // 2
    middle = category[middleIndex]

    if limit > middle[1]:
        findPartition(limit, middleIndex + 1, destination, category)
    elif limit <= middle[1]:
        findPartition(limit, start, middleIndex, category)


for _ in range(categoryNum):
    categoryName, powerLimit = map(str, input().split(' '))
    category.append((categoryName, int(powerLimit)))


inputPowerList = list(int(input()) for _ in range(M))
done = {}

for limit in inputPowerList:
    if limit not in done:
        findPartition(limit, 0, len(category)-1, category)
    else:
        print(done[limit])