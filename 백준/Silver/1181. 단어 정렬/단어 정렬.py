N = int(input())

arr = list()

for i in range(N):
    arr.append(input())
    
arr = list(set(arr))


arr.sort()              #알파벳 순 정렬
arr.sort(key = len)     #길이 순 정렬 (알파벳 순 정렬되어있는 상태로 길이 같으면 패스)



for word in arr:
    print(word)