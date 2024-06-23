import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
houses = []
chickenAll = []
total_chicken_distance = 0

#입력받기
for i in range(N):
    for j in range(N):
        if(arr[i][j] == 1):
            houses.append([i,j])
        elif(arr[i][j] == 2):
            chickenAll.append([i,j])



#최대 M개 선택
def MinDistance():
    global total_chicken_distance
    min_total_distance = 100000

    c_len = len(chickenAll)
    for i in range(1, 1 << c_len):
        res = []
        for j in range(c_len):
            if(i & (1 << j)):
                res.append(chickenAll[j])
        
        if(len(res) != M): continue


        total_chicken_distance = 0


        for house in houses:
            MIN_DISTANCE = 100000
            for selectedChicken in res:
                dis = abs(house[0] - selectedChicken[0])\
                        +abs(house[1] - selectedChicken[1])

                if(MIN_DISTANCE > dis):
                    MIN_DISTANCE = dis

            total_chicken_distance += MIN_DISTANCE
            
        if(min_total_distance > total_chicken_distance):
            min_total_distance = total_chicken_distance
    return min_total_distance




print(MinDistance())