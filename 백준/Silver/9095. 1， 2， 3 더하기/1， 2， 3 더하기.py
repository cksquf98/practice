import sys
input = sys.stdin.readline

T = int(input())
dp = [0 for _ in range(11)] #dp[n] = 숫자 n을 만드는 방법의 수, 문제에서 n은 11보다 작다고 했음

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(T):
    n = int(input())
    print(dp[n])