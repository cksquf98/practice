import sys
input = sys.stdin.readline

N = int(input())  # 예산 요청 지방 수
budgetList = list(map(int, input().split(' ')))  # 지방의 예산요청 금액 리스트
budgetList.sort()

totalBudget = int(input())  # 총 예산
standard = totalBudget // len(budgetList)
maxPrice = 0

def check(standard, budgetList):
    for budget in budgetList:
        if standard >= budget:
            return True

i = 0
while i < N:
    # print("standard = ",standard)
    if budgetList[i] <= standard:
        maxPrice = budgetList[i]
        totalBudget -= budgetList[i]
    elif budgetList[i] > standard:
        standard = totalBudget // (N - i) # 새로운 상한액
        # print("new standard = ", standard)

        if check(standard, budgetList[i:]):
            # print("True")
            i = i-1
        else:
            maxPrice = standard
            break
    
    i += 1
print(maxPrice)