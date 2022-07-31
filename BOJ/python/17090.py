# 문제
# 크기가 N×M인 미로가 있고, 미로는 크기가 1×1인 칸으로 나누어져 있다. 미로의 각 칸에는 문자가 하나 적혀있는데, 적혀있는 문자에 따라서 다른 칸으로 이동할 수 있다.
#
# 어떤 칸(r, c)에 적힌 문자가
#
# U인 경우에는 (r-1, c)로 이동해야 한다.
# R인 경우에는 (r, c+1)로 이동해야 한다.
# D인 경우에는 (r+1, c)로 이동해야 한다.
# L인 경우에는 (r, c-1)로 이동해야 한다.
# 미로에서 탈출 가능한 칸의 수를 계산해보자. 탈출 가능한 칸이란, 그 칸에서 이동을 시작해서 칸에 적힌대로 이동했을 때, 미로의 경계 밖으로 이동하게 되는 칸을 의미한다.
#
# 입력
# 첫째 줄에 미로의 크기 N, M(3 ≤ N, M ≤ 500)이 주어진다. 둘째 줄부터 N개의 줄에는 미로의 각 칸에 적힌 문자가 주어진다.
#
# 출력
# 첫째 줄에 탈출 가능한 칸의 수를 출력한다.
import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
grid = [list(str(input())) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
mapping = {'R': 0, 'D': 1, 'L': 2, 'U': 3}
def find_dest(y, x):
    global answer
    d = mapping[grid[y][x]]
    ny, nx = y+dy[d], x+dx[d]
    if 0 <= ny < n and 0 <= nx < m:
        if not dp[ny][nx]:
            dp[y][x] = -1
            dp[y][x] = find_dest(ny, nx)
        else:
            dp[y][x] = dp[ny][nx]
        return dp[y][x]
    return 1
answer = 0
for i in range(n):
    for j in range(m):
        if not dp[i][j]:
            dp[i][j] = -1
            dp[i][j] = find_dest(i, j)
        if dp[i][j] == 1:
            answer += 1
print(answer)
