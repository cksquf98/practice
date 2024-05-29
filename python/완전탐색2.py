'''
언덕 개수N, 각 언덕의 최고-최저 높이 차가 17이하여야 스키장 등록 가능
언덕의 높이는 0~100까지 정수
언덕 높이 x만큼 변경하는데 x^2비용 듬
언덕 높이 변경하는 "최소 비용" 구하기
'''

N = int(input('언덕 개수 :'))
hills = list()
for i in range(N):
    hill = int(input('언덕 높이 :'))
    hills.append(hill)

MAX_DIFFERENCE = 17
MAX_HILL_HEIGHT = 100

def givenRangeCost(hills,lowHill,highHill):
    '''
    언덕의 높이를 low ~ high 범위로 변경한 총 비용 반환
    '''
    cost = 0
    for hill in hills:
        if(hill < lowHill):
            cost += (lowHill - hill)**2
        elif(hill > highHill):
            cost += (hill-highHill)**2
    return cost

minCost = 99999999999

for lowHill in range(1, MAX_HILL_HEIGHT+1):
    resultCost = givenRangeCost(hills,lowHill , lowHill+MAX_DIFFERENCE)
    if(resultCost < minCost):
        minCost = resultCost