import sys
input = sys.stdin.readline

N = int(input())

dp = [0 for _ in range(11)] #dp[n] = 숫자 n을 만드는 방법의 수, 문제에서 11보다 작다고 했음
 
"""
DP = 규칙성 찾기

    1 --> 1
    2 --> 1+1
          2
    3 --> 1+1+1
          2+1
          1+2
          3

    4 --> +1 연산: 3만든 식에 +1
          1+1+1+1
          2+1+1
          1+2+1
          3+1
          -----------------
          +2 연산: 2만든 식에 +2
          1+1+2
          2+2
          -----------------
          +3 연산: 1만든 식에 +3
          1+3

    5 --> +1 연산: 4만든 식에 +1
          1+1+1+1+1
          2+1+1+1
          1+2+1+1
          3+1+1
          1+1+2+1
          2+2+1
          1+3+1
          -----------------
          +2 연산: 3만든 식에 +2
          1+1+1+2
          2+1+2
          1+2+2
          3+2
          -----------------
          +3 연산: 2만든 식에 +3
          1+1+3
          2+3


i 만드는 연산 개수 = i-1 연산 개수+ i-2 연산 개수 + i-3 연산 개수
DP[i] = DP[i-1] + DP[i-2] + DP[i-3]
"""

dp[1] = 1
dp[2] = 2
dp[3] = 4 

for i in range(4, 11):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]


for _ in range(N):
    num = int(input())
    print(dp[num])
