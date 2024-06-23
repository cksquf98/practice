#재료 N개 - 각 재료의 신맛 S, 쓴맛 B
#음식의 신맛 = 재료 신맛 곱
#음식의 쓴맛 = 재료 쓴맛 합

#재료는 적어도 하나 사용, 신맛과 쓴맛의 차이가 가장 작은 요리 구하기

#어 이거 부분집합인데 공집합 없도록
import sys
input = sys.stdin.readline

N = int(input())
ingredient = []
min = 100000000


result = []
def Subset():
    
    for i in range(1 << N):
        res = []
        for j in range(N):
            if(i & (1 << j)):
                res.append(ingredient[j])
        result.append(res)
    



for i in range(N):
    ingredient.append(list(map(int, input().split())))


Subset()


min = 1000000000
for igd_subset in result:
    sin = 1
    bitter = 0

    if(len(igd_subset) == 0): continue
    
    for igd in igd_subset:
        sin *= igd[0]
        bitter += igd[1]
    
    if(abs(sin - bitter) < min):
        min = abs(sin - bitter)

print(min)