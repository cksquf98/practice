import sys
# from collections import deque
input = sys.stdin.readline

rest = input().rstrip()  # 남은 수를 한 줄로 이어 붙인 수


# N의 최솟값을 구해야 함!!
predictionOfN = 0
index = 0

while index < len(rest):
    predictionOfN += 1
    predictionOfN_string = str(predictionOfN)
    # print("predictionOfN = ",predictionOfN)

    for i in range(len(predictionOfN_string)):
        if index < len(rest) and rest[index] == predictionOfN_string[i]:
            # print("index, rest = ", index, rest[index])
            index += 1
            # print("한자리라도 포함된 경우의 predictionOfN = ", predictionOfN)

print(predictionOfN)
