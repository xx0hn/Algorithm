# 문제
# With plenty of free time on their hands (or rather, hooves), the cows on Farmer John's farm often pass the time by playing video games. One of their favorites is based on a popular human video game called Puyo Puyo; the cow version is of course called Mooyo Mooyo.
#
# The game of Mooyo Mooyo is played on a tall narrow grid $N$ cells tall ($1 \leq N \leq 100$) and 10 cells wide. Here is an example with $N = 6$:
#
# 0000000000
# 0000000300
# 0054000300
# 1054502230
# 2211122220
# 1111111223
# Each cell is either empty (indicated by a 0), or a haybale in one of nine different colors (indicated by characters 1..9). Gravity causes haybales to fall downward, so there is never a 0 cell below a haybale.
#
# Two cells belong to the same connected region if they are directly adjacent either horizontally or vertically, and they have the same nonzero color. Any time a connected region exists with at least $K$ cells, its haybales all disappear, turning into zeros. If multiple such connected regions exist at the same time, they all disappear simultaneously. Afterwards, gravity might cause haybales to fall downward to fill some of the resulting cells that became zeros. In the resulting configuration, there may again be connected regions of size at least $K$ cells. If so, they also disappear (simultaneously, if there are multiple such regions), then gravity pulls the remaining cells downward, and the process repeats until no connected regions of size at least $K$ exist.
#
# Given the state of a Mooyo Mooyo board, please output a final picture of the board after these operations have occurred.
#
# 입력
# The first line of input contains $N$ and $K$ ($1 \leq K \leq 10N$). The remaining $N$ lines specify the initial state of the board.
#
# 출력
# Please output $N$ lines, describing a picture of the final board state.
import copy
from collections import deque
n, k = map(int, input().split())
grid = [list(str(input())) for _ in range(n)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    path = [(y, x)]
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < 10 and not visited[ny][nx] and grid[ny][nx] == grid[y][x]:
                visited[ny][nx] = True
                path.append((ny, nx))
                q.append((ny, nx))
    if len(path) >= k:
        for py, px in path:
            grid[py][px] = '0'
def drop_nums():
    global grid
    new_grid = [['0' for _ in range(10)] for _ in range(n)]
    for i in range(10):
        idx = n-1
        for j in range(n-1, -1, -1):
            if grid[j][i] != '0':
                new_grid[idx][i] = grid[j][i]
                idx -= 1
    grid = copy.deepcopy(new_grid)
while True:
    visited = [[False for _ in range(10)] for _ in range(n)]
    tmp = copy.deepcopy(grid)
    for i in range(n):
        for j in range(10):
            if grid[i][j] and not visited[i][j]:
                bfs(i, j)
    drop_nums()
    if tmp == grid:
        break
for i in range(n):
    print(''.join(grid[i]))
