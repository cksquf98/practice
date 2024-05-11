N = int(input())

arr = []

for i in range(N):
    a,b = map(int,input().split())
    l = list()
    l.append(a)
    l.append(b)
    arr.append(l)

arr.sort()
arr.sort(key= lambda x : x[1])

for num1, num2 in arr:
    print(num1, num2)