# 문제 조건: 1 ≤ k ≤ 14 / 1 ≤ n ≤ 14

import sys
input = sys.stdin.readline

T = int(input())
dp = [[0]*15 for _ in range(15)]

#0층은 0,1,2,3,4 ..
dp[0] = [i for i in range(15)]

for i in range(1,15):
    for j in range(1,15):
        dp[i][j] = dp[i][j-1]+dp[i-1][j]

for _ in range(T):
    k = int(input())
    n = int(input())
    print(dp[k][n])