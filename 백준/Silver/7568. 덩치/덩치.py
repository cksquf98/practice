"""
문제 이해를 잘못했다!!! 등수가 모든 사람과 비교했을때의 등수래
정렬하려고 했는데 브루트포스로 해야되나봣
"""

import sys
input = sys.stdin.readline

# 사람의 수
N = int(input())

# 키 몸무게 입력
heigtAndWeightList = [list(map(int, input().split(' '))) for _ in range(N)]

ranking = {}

for i in range(N):
    rank = 1
    for j in range(N):
        if (heigtAndWeightList[i][0] < heigtAndWeightList[j][0] and
           heigtAndWeightList[i][1] < heigtAndWeightList[j][1]):
            rank += 1

    ranking[i] = rank

for i in range(N):
    print(ranking[i], end=' ')