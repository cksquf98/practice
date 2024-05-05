import sys

N = int(sys.stdin.readline().rstrip())
dance = {"ChongChong"}

for i in range(N):
    s1, s2 = sys.stdin.readline().rstrip().split()
    if (s1 in dance):
        dance.add(s2)
    elif (s2 in dance):
        dance.add(s1)

print(len(dance))