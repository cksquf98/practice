import sys
input = sys.stdin.readline

"""
1 = 1 => 1개
2 = 1+1 / 2 => 2개
3 = 1+1+1 / 2+1 / 3 => 3개


4 = 1+1+1+1 / 2+1+1 / 2+2 / 3+1 => 4개
5 = 4개 + (3+2 , 2+3) => 5개
6 = 5 방법에 1 더하기 + 2+2+2 / 3+3 => 7개 **
7 = 6 방법에 1 더하기 + 2+2+3 => 8개
8 = (7) +1 / 2+2+2+2 / 2+3+3 => 10개
9 = (8) +1 / 2+2+2+3 / 3+3+3 => 12개 **
10 = (9) +1 / 2+2+2+2+2 / 2+2+3+3 => 14개
"""

T = int(input())

dp = [0] * 10001

dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(4, 10001):
    if i % 3 == 0:
        dp[i] = dp[i-2] + dp[i-1] - dp[i-3] + 1
    else:
        dp[i] = dp[i-2] + dp[i-1] - dp[i-3]

for _ in range(T):
    num = int(input())
    print(dp[num])