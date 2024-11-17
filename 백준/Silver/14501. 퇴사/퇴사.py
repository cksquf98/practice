import sys
input = sys.stdin.readline

N = int(input())  # 퇴사까지 남은 날 수
day = [0] * (N + 1)
price = [0] * (N + 1)

for i in range(1, N + 1):
    T, P = map(int, input().split())
    day[i] = T
    price[i] = P

max_price = 0  # 최대 수익

def dfs(current_day, total_price):
    global max_price

    # 현재 날짜가 퇴사일 이후일 경우 종료
    if current_day > N:
        max_price = max(max_price, total_price)
        return

    # 상담을 하지 않는 경우 (다음 날짜로 이동)
    dfs(current_day + 1, total_price)

    # 상담을 수행하는 경우 (유효한 날짜만)
    if current_day + day[current_day] - 1 <= N:
        dfs(current_day + day[current_day], total_price + price[current_day])

# 탐색 시작
dfs(1, 0)
print(max_price)
