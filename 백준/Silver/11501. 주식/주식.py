import sys
input = sys.stdin.readline

T = int(input())  # 테스트 케이스 수

for _ in range(T):
    N = int(input())  # 주가 수
    stockList = list(map(int, input().split(' ')))

    maxStock = 0
    result = 0
    # 내가 전에 했던 남은 리스트에서 다시 max를 찾는 로직은 시간초과가 났도다
    # 미래를 알고있다는 가정 -> 역순으로 탐색 -> 본인이 최댓값이면 차액을 result에 누적하고, 더 큰애가 나오면 걔를 최댓값으로 설정
    for i in range(N-1, -1, -1):
        if stockList[i] < maxStock:
            result += maxStock - stockList[i]
        else:
            maxStock = stockList[i]

    print(result)
