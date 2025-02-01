import sys
input = sys.stdin.readline

N = int(input())  # 도시의 개수
distance = list(map(int, input().split(' ')))  # 연결하는 도로의 길이 = N - 1개
oilPrice = list(map(int, input().split(' ')))  # 주유소의 리터당 가격 = N개

currentPrice = 0
currentOilPrice = oilPrice[0] # 더 싼 주유소가 있으면 갱신되도록?!
for i in range(N-1):
    if currentOilPrice > oilPrice[i]:
        currentPrice += oilPrice[i] * distance[i]
        currentOilPrice = oilPrice[i]
    else:
        currentPrice += currentOilPrice * distance[i]

print(currentPrice)