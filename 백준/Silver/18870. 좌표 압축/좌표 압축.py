# def printIndex(arr, elem):
#     index = 0
#     for i in arr:
#         if(elem == i):
#             return index
#         else:
#             index+=1
#     return -1


import sys

input = sys.stdin.readline

N = int(input())

input = list(map(int, input().split()))

sortedInput = list(set(input))
sortedInput.sort()


# 하나하나 비교하는 방식으로는 O(N) -> 시간 초과 뜸
# for i in range(N):
#     count = printIndex(sortedInput, input[i])
#     print(count, end=' ')

dic = {sortedInput[i] : i for i in range(len(sortedInput))}

# ex)  sortedInput = [-10, -9, 2, 4]
#      dic = {-10 :0, -9 : 1, 2 :2, 4 :3}

for i in input:
    print(dic[i], end=' ')