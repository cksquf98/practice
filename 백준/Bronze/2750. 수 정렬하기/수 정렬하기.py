import sys
input = sys.stdin.readline

#선택정렬
N = int(input())

arr = [0 for _ in range(N)]
for i in range(N):
    arr[i] = int(input())

#최솟값을 가진 인덱스가 0이라고 가정하고 스타트
for i in range(N-1):
    minIdx = i
    for j in range(i+1,N):
        #탐색중인애 다음 원소들 중 최솟값을 가진 원소의 인덱스로 갱신
        if(arr[j] < arr[minIdx]):
            minIdx = j
    
    #탐색 시작한 위치랑 교환
    tmp = arr[i]
    arr[i] = arr[minIdx]
    arr[minIdx] = tmp

for elem in arr:
    print(elem)