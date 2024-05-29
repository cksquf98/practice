'''
마을의 크기 : (오른쪽 마을 위치 - 기준)/2 - (기준 - 왼쪽 마을 위치)/2
마을의 위치 : 위치 순서대로 정렬
가장자리 마을은 제외
가장 작은, 마을의 크기는? (소수점 첫째 자리까지)
'''

village_num = int(input('마을의 수 : '))
village = []

for i in range(village_num):
    # v = int(input('마을 위치 : '))
    # village.append(v)
    village.append(int(input('마을 위치 : ')))

# 리스트.sort(reverse = True) : 내림차순 정렬
village.sort()          

# 반복문 돌면서 최솟값 계산
i = 1
min_size = 1000000

while(i < len(village)-1):
    size = (village[i+1]-village[i])/2 + (village[i]-village[i-1])/2
    if(size < min_size):
        min_size = size
        smallest_v = village[i]
    i+=1

print(f'가장 작은 마을은 {smallest_v}이고, 최솟값은 {min_size}')
# 2로 나누기 때문에, 당연히 n.0 or n.5의 결과가 나옴 => 따로 소수점 처리할 필요 없음