import sys
input = sys.stdin.readline

N = int(input())
optionList = [input().rstrip() for _ in range(N)]
shortcut = {}
reverse_shortcut = {}


for option in optionList:
    splitWord = list(map(str, option.split(" ")))
    flag = True
    # 단어 첫글자
    for i in range(len(splitWord)):
        word = splitWord[i]
        if word[0].lower() not in shortcut:
            shortcut[word[0].lower()] = True
            word = "[" + word[0] + "]" + word[1:]
            splitWord[i] = word
            reverse_shortcut[option] = " ".join(splitWord)
            flag = False
            break

    #  왼쪽에서부터 차례대로 알파벳
    if flag:
        res = option
        i = 0
        for char in option:
            if char == " ":
                i+=1
                continue

            if char.lower() not in shortcut:
                shortcut[char.lower()] = True
                word = option[:i] + "[" + option[i] + "]" + option[i+1:]
                res = word
                break

            i += 1
        reverse_shortcut[option] = res

    print(reverse_shortcut[option])