import sys
import heapq
input = sys.stdin.readline

N,C = map(int, input().split())
message = list(map(int, input().split()))


freq = {}

for idx in range(len(message)):
    elem = message[idx]
    if(freq.get(elem) == None):
        freq[elem] = [1, idx]
    else:
        freq[elem][0] += 1

# print(freq)
freq = sorted(freq.items(), key=lambda x:(x[1][0], -x[1][1]), reverse=True)
# print(freq)

for k, v in freq:
    fq = v[0]
    for _ in range(fq):
        print(k, end=" ")
print()