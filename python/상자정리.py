'''
1. 입력값 정리 필요 : n = 박스 개수 input > n줄 박스 input
                     k = 피규어 개수 input > 그 줄에 k개의 높이 입력
2. 입력받은 상자 내 피규어 정렬 확인
3. 각 상자 양 끝의 피규어 높이 체크 리스트 생성
4. 새로운 상자들 정렬
5. 정렬된 상자들을 정리할 수 있는지 체크
'''

def readBox(n):
    box_list = []
    for i in range(n):
        box = input('피규어 개수 및 높이 : ').split()
        box.pop(0)
        box_list(box)
    return box_list

def checkHeight_pg(box_list):
    for box in box_list:
        for j in range(len(box[j])-1):
            if(box[j] > box[j+1]):
                return False
    return True

def CreateEndPoint(box_list):
    endPoint = []
    for box in box_list:
        endPoint.append(box[0],box[-1])
    return endPoint

def CheckEndPoint(endPoint):
    # endPoint리스트는 두개의 값 리스트임 [ a , b ] 
    # => 최댓값을 젤 작은 박스의 최댓값으로 설정하고 오른쪽 박스 최솟값이랑 돌려가면서 비교
    max = endPoint[0][1]  
    for i in range(len(endPoint)-1):
        if(max > endPoint[i][0]):
            return False
        else:
            max = endPoint[i][1]
    return True

n = int(input('상자 개수 : '))
box_list = readBox(n)

# 상자 내 피규어 높이가 오름차순 아닌 애들 거르기
if(not checkHeight_pg(box_list)):
    print("wrong PG height input")
else:
    # 양 끝 피규어 높이를 저장하는 리스트를 따로 만들어서 얘네를 sort
    endPoint = CreateEndPoint(box_list).sort()
    if CheckEndPoint(endPoint):
        print("정리 가능")
    else:
        print("정리 불가능")
    