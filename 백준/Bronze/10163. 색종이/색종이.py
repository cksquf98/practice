import sys
input = sys.stdin.readline


paper = [[0] * 1001 for _ in range(1001)] #가로 1001, 세로 1001
N = int(input())

for i in range(N):
    x, y, width, height = map(int, input().split())
    
    for w in range(x, x + width):
        for h in range(y, y+height):
            paper[w][h] = i+1
            

for p in range(1, N+1):
    ans = 0
    
    for i in range(1001):
        for j in range(1001):
            if(paper[i][j] == p):
                ans += 1 
           
    print(ans)