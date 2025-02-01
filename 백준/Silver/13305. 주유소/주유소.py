# 여기서 남은 거리까지 다 넣고 가는 비용이랑, 각자 따로 넣었을때 비용이랑 비교히면 어떨까
import sys
input = sys.stdin.readline

N = int(input())  # 도시의 개수
distance = list(map(int, input().split(' ')))  # 연결하는 도로의 길이 = N - 1개
oilPrice = list(map(int, input().split(' ')))  # 주유소의 리터당 가격 = N개


price = 0
totalDistance = 0
for i in range(N-1):
    price += oilPrice[i] * distance[i]
    totalDistance += distance[i]

currentPrice = 0
for i in range(N-1):
    comparePrice = currentPrice + oilPrice[i] * totalDistance
    if comparePrice < price:
        price = comparePrice

    currentPrice += oilPrice[i] * distance[i]
    totalDistance -= distance[i]

print(price)