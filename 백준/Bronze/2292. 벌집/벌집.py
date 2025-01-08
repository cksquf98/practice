import sys

input = sys.stdin.readline

N = int(input())

# 벌집 : 육각형
# 첫번째 벌집 : 1
# 두번째 줄 벌집 : 2~7 (6개)
# 세번째 줄 벌집 : 8~19 (12개)
# 네번째 줄 벌집 : 20~37 (18개)
# 다섯번째 줄 벌집 : 38~63 (24개)
# ...

# 주어지는 벌집방까지 몇개의 벌집을 거쳐서 가야하는가
# ex. 13 <<세번째 줄 벌집
# ex. 58 <<다섯번째 줄 벌집
# 6의 배수로 얼마나 나뉘는지 -> 나머지가 있으면 쭉쭉 나눠서 나누는 수보다 작아질때까지
# 나뉜 카운트가 벌집 줄 수

currentNum = N
level = 1

# 첫번째 벌집은 따로 처리!!
if (currentNum == 1):
    print(1)
else:
    # 두번째 줄부터
    currentNum -= 1
    while currentNum > 0:
        currentNum -= level * 6
        level += 1

    print(level)
