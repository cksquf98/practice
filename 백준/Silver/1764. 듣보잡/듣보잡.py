import sys

N, M = map(int,sys.stdin.readline().split())
dic = {}
print_list = []

for i in range(N):
    hear_name = sys.stdin.readline().rstrip()
    dic[hear_name] = 1

for j in range(M):
    see_name = sys.stdin.readline().rstrip()
    if(dic.get(see_name) != None):
        print_list.append(see_name)
    else:
        continue

print(len(print_list))
for n in sorted(print_list):
    print(n)