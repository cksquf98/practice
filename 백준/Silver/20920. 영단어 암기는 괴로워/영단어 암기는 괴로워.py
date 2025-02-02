import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))  # N은 단어 개수, M은 최소글자 수

words = []
wordCount = {}

for i in range(N):
    word = input().rstrip()

    if len(word) < M:
        continue

    if wordCount.get(word) != None:
        wordCount[word] += 1
    elif wordCount.get(word) == None:
        words.append(word)
        wordCount[word] = 1


words.sort(key=lambda x: (-wordCount[x], -len(x), x))

for word in words:
    print(word)