# 엥 문제가 자리를 재배치할 수 없다는데? 그럼 제대로 말하던가 ㅡㅡ 사전순 출력이라길래 정렬해야하는건줄 알앗잖아. 원본 문자열에서 0을 최대한 앞에 남게하고 1은 뒤에 남게 없애래
import sys
input = sys.stdin.readline

S = input().rstrip()
SList = list(S)

zeroCount = S.count('0') // 2
oneCount = S.count('1') // 2

for i in range(len(SList)):  # 앞에서부터 돌면서 1 반만큼 제거
    if oneCount <= 0:
        break
    if SList[i] == '1':
        SList[i] = '2'
        oneCount -= 1

for j in range(len(SList)-1, -1, -1):  # 뒤에서부터 돌면서 0 반만큼 제거
    if zeroCount <= 0:
        break
    if SList[j] == '0':
        SList[j] = '2'
        zeroCount -= 1

result = ''
for char in SList:
    if char != '2':
        result += char

print(result)