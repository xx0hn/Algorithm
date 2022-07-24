# 문제
# 크기가 R×C인 체스판이 있고, 체스판의 각 칸에는 정수가 하나씩 적혀있다. 체스판에 적혀있는 정수는 모두 서로 다르다.
#
# 체스판의 각 칸 위에 공을 하나씩 놓는다. 이제 공은 다음과 같은 규칙에 의해서 자동으로 움직인다.
#
# 인접한 8방향 (가로, 세로, 대각선)에 적힌 모든 정수가 현재 칸에 적힌 수보다 크면 이동을 멈춘다.
# 그 외의 경우에는 가장 작은 정수가 있는 칸으로 공이 이동한다.
# 공의 크기는 매우 작아서, 체스판의 한 칸 위에 여러 개의 공이 있을 수 있다. 체스판의 상태가 주어진다. 공이 더 이상 움직이지 않을 때, 각 칸에 공이 몇 개 있는지 구해보자.
#
# 입력
# 첫째 줄에 체스판의 크기 R, C가 주어진다. 둘째 줄부터 R개의 줄에 체스판에 적혀있는 정수가 주어진다.
#
# 출력
# 총 R개의 줄에 걸쳐서 체스판에 적힌 정수를 출력한다.
#
# 제한
# 1 ≤ R, C ≤ 500
# 0 ≤ 체스판에 적힌 정수 ≤ 300,000
from collections import deque
r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]
marbles = [[1 for _ in range(c)] for _ in range(r)]
parent = [[[] for _ in range(c)] for _ in range(r)]
dy, dx = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
def bfs(sy, sx):
    q = deque()
    q.append((sy, sx))
    while q:
        y, x = q.popleft()
        mn, idx = 1e9, []
        for i in range(8):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < r and 0 <= nx < c:
                if grid[ny][nx] <= grid[y][x] and mn >= grid[ny][nx]:
                    mn = grid[ny][nx]
                    idx = [ny, nx]
        if mn == 1e9 and not idx:
            return [y, x]
        if parent[idx[0]][idx[1]]:
            return parent[idx[0]][idx[1]]
        else:
            q.append((idx[0], idx[1]))
for i in range(r):
    for j in range(c):
        parent[i][j] = bfs(i, j)
new_marbles = [[0 for _ in range(c)] for _ in range(r)]
for i in range(r):
    for j in range(c):
        if marbles[i][j]:
            nxt_idx = parent[i][j]
            new_marbles[nxt_idx[0]][nxt_idx[1]] += marbles[i][j]
for i in range(r):
    print(*new_marbles[i])
