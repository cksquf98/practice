if __name__=="__main__":
    import sys
    from itertools import combinations

    input = sys.stdin.readline
    N, M = map(int, input().split())
    num = [i for i in range(1, N+1)]

    for perm in combinations(num, M):
        for i in perm:
            print(i, end = ' ')
        print()