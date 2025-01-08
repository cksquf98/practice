import sys

input = sys.stdin.readline

word = input().upper().rstrip()

wordCount = {}

for alphabet in word:
    if(wordCount.get(alphabet) != None):
        wordCount[alphabet] += 1
    else:
        wordCount[alphabet] = 1


max_count = 0
result = ''

for alphabet in wordCount:
    if(wordCount[alphabet] > max_count):
        result = alphabet
        max_count = wordCount[alphabet]
    elif(wordCount[alphabet] == max_count):
        result = '?'

print(result)