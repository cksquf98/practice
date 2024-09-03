"""
하노이탑 알고리즘 유툽 다시 봐야겠다
"""

def hanoi(n, start, temp, end):
    if n == 1:
        print(start, end)
        return
    
    hanoi(n-1, start, end, temp) #A->B
    print(start, end) #가장 큰 원판 옮기기
    hanoi(n-1, temp, start, end) #B->C

if __name__=="__main__":
    import sys
    input = sys.stdin.readline

    N = int(input())
    print(pow(2,N)-1)
    hanoi(N, 1, 2, 3)