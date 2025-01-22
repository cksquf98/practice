import sys
input = sys.stdin.readline

moeumList = {"a", "e", "i", "o", "u"}


def moeum_check(word):
    # 모음 있는지 여부 체크
    for alphabet in word:
        if (alphabet in moeumList):
            return True
    return False


def is_acceptable(word):
    # 모음 있는지 여부 체크
    if not moeum_check(word):
        return False

     # 연속적인 글자 체크 - ee, oo 예외
    for i in range(len(word)-1):
        if word[i] not in {"e", "o"} and word[i] == word[i+1]:
            return False

    """
    *** 연속적인 모음 / 연속적인 자음 체크 ***
    기존에 생각한건 3글자중에 하나라도 모음이 있으면 연속 자음이 아니니까 ㄱㅊ지 않나?했던건데
    이러면 "aeo"이런애들 체크를 못하넴
    """
    moeumCount = 0
    jaeumCount = 0

    for alphabet in word:
        if alphabet in moeumList:
            jaeumCount = 0
            moeumCount += 1
        else:
            moeumCount = 0
            jaeumCount += 1

        if moeumCount == 3 or jaeumCount == 3:
            return False

    return True


while True:
    word = input().rstrip()

    if word == 'end':
        break

    if (is_acceptable(word)):
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")
