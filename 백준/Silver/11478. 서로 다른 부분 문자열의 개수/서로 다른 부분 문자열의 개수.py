import sys

word = sys.stdin.readline().rstrip()
word_set = set()

length = len(word)
interval = 0
while(interval < length):
    for i in range(0, length-interval):
        word_set.add(word[i:i+interval+1])
        # print(word[i:i+interval+1])

    interval += 1


print(len(word_set))