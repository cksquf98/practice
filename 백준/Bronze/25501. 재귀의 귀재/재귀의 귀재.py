recursion_cnt = 0


def recursion(s, l, r):
    global recursion_cnt    #전역변수 접근 방법!!!!! global 키워드
    recursion_cnt += 1

    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    global recursion_cnt
    recursion_cnt = 0
    return recursion(s, 0, len(s)-1)


import sys

N = int(sys.stdin.readline())
for i in range(N):
    print(isPalindrome(sys.stdin.readline().rstrip()), recursion_cnt)