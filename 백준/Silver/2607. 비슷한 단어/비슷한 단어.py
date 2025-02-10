import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())  # 단어 개수

standard = input().rstrip()  # 비슷한 단어 찾는 기준이 될 단어
standardLetter = set()

for letter in standard:
    standardLetter.add(letter)  # 단어 문자 분리


def checkWord(standard, word, standardLetter):
    wordLength = len(word)
    # 한 문자 빼기
    if wordLength == len(standard) + 1:
        for i in range(wordLength):
            copy = word[:i] + word[i+1:]

            if Counter(copy) == Counter(standard):
                return True

    # 한 문자 더하기
    elif wordLength == len(standard) - 1:
        for letter in standardLetter:
            for i in range(len(standard)):
                copy = list(word)
                copy.insert(i, letter)

                if Counter(copy) == Counter(standard):
                    return True

    # 한 문자를 다른 문자로
    elif wordLength == len(standard):
        for i in range(wordLength):
            copy = list(word)
            for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                copy[i] = char

                if Counter(copy) == Counter(standard):
                    return True

    return False


count = 0
for _ in range(N-1):
    wordLetter = set()
    word = input().rstrip()

    for letter in word:
        wordLetter.add(letter)

    # 같은 구성
    if Counter(word) == Counter(standard):
        count += 1

    # 한 단어에서 한 문자를 더하거나, 빼거나, 하나의 문자를 다른 문자로 바꾸어 나머지 한 단어와 같은 구성을 갖게 되는 경우
    elif checkWord(standard, word, standardLetter):
        count += 1
    else:
        continue

print(count)
