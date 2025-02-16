import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
keyword = set()

for _ in range(N):
    word = input().rstrip()
    keyword.add(word)

for _ in range(M):
    blog_keyword = list(input().rstrip().split(','))

    for word in blog_keyword:
        if word in keyword:
            keyword.remove(word)

    print(len(keyword))