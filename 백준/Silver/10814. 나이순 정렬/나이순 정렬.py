N = int(input())

arr = []

for i in range(N):
    age, name = input().split()
    
    a = list()
    a.append(int(age))
    a.append(name)
    arr.append(a)

arr.sort(key = lambda x: x[0])

for age, name in arr:
    print(age, name)