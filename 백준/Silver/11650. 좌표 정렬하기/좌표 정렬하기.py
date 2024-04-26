N = int(input())

num = []

for i in range(N):
    A,B = map(int,input().split())
    a = list()
    a.append(int(A))
    a.append(int(B))
    num.append(a)


num.sort()
for num1, num2 in num:
    print(num1,num2)