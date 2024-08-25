def factorial(N):
    if N > 1:
        return (N * factorial(N-1))
    else:
        return 1

T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split()))
    print (factorial(M) //  (factorial(M-N) * factorial(N)))