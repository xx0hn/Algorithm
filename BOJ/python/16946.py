# 문제
# N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 한 칸에서 다른 칸으로 이동하려면, 두 칸이 인접해야 한다. 두 칸이 변을 공유할 때, 인접하다고 한다.
#
# 각각의 벽에 대해서 다음을 구해보려고 한다.
#
# 벽을 부수고 이동할 수 있는 곳으로 변경한다.
# 그 위치에서 이동할 수 있는 칸의 개수를 세어본다.
# 한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다.
#
# 출력
# 맵의 형태로 정답을 출력한다. 원래 빈 칸인 곳은 0을 출력하고, 벽인 곳은 이동할 수 있는 칸의 개수를 10으로 나눈 나머지를 출력한다.
from collections import deque, defaultdict
n, m = map(int, input().split())
grid = [list(str(input())) for _ in range(n)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
answer = [['0' for _ in range(m)] for _ in range(n)]
groups = defaultdict(int)
num = 2
def make_groups(y, x):
    q = deque()
    q.append((y, x))
    grid[y][x] = str(num)
    cnt = 1
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny, nx = cy+dy[i], cx+dx[i]
            if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] == '0':
                grid[ny][nx] = str(num)
                cnt += 1
                q.append((ny, nx))
    return cnt
for i in range(n):
    for j in range(m):
        if grid[i][j] == '0':
            groups[str(num)] = make_groups(i, j)
            num += 1
        if grid[i][j] == '1':
            answer[i][j] = '1'
for i in range(n):
    for j in range(m):
        if grid[i][j] == '1':
            tmp = []
            for d in range(4):
                ni, nj = i+dy[d], j+dx[d]
                if 0 <= ni < n and 0 <= nj < m:
                    if grid[ni][nj] != '1' and grid[ni][nj] not in set(tmp):
                        tmp.append(grid[ni][nj])
            for group in tmp:
                answer[i][j] = str((int(answer[i][j])+groups[group])%10)
for i in range(n):
    print(''.join(answer[i]))
