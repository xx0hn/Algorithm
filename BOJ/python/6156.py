# 문제
# N (1 <= N <= 100) cows, conveniently numbered 1..N, are participating in a programming contest. As we all know, some cows code better than others. Each cow has a certain constant skill rating that is unique among the competitors.
#
# The contest is conducted in several head-to-head rounds, each between two cows. If cow A has a greater skill level than cow B (1 <= A <= N; 1 <= B <= N; A != B), then cow A will always beat cow B.
#
# Farmer John is trying to rank the cows by skill level. Given a list the results of M (1 <= M <= 4,500) two-cow rounds, determine the number of cows whose ranks can be precisely determined from the results. It is guaranteed that the results of the rounds will not be contradictory.
#
# 입력
# Line 1: Two space-separated integers: N and M
# Lines 2..M+1: Each line contains two space-separated integers that describe the competitors and results (the first integer, A, is the winner) of a single round of competition: A and B
# 출력
# Line 1: A single integer representing the number of cows whose ranks can be determined
n, m = map(int, input().split())
grid = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    grid[a][b] = 1
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if grid[i][j] == 0:
                if grid[i][k] and grid[k][j]:
                    grid[i][j] = 1
answer = 0
for i in range(1, n+1):
    w, l = 0, 0
    for j in range(1, n+1):
        if grid[i][j] == 1:
            w += 1
        if grid[j][i] == 1:
            l += 1
    if w+l == n-1:
        answer += 1
print(answer)
