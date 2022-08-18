# 문제
# 빈 공간, 벽, 그리고 두 명의 플레이어 A와 B의 시작지점이 주어졌을 때, A와 B가 서로의 위치를 바꾸는데 드는 턴의 최솟값을 구하는 프로그램을 작성하시오.
#
# 한 턴에 하나 또는 두 명의 플레이어는 움직일 수 있다. 한 번 움직인다는 것은 현재 위치에서 위, 왼쪽, 오른쪽, 아래, 4가지 대각선 중 하나로 이동하는 것이다. 하지만, 벽으로 이동하거나, 게임 판을 벗어나게 이동할 수는 없다. 그리고 각 턴의 마지막에 두 플레이어는 같은 곳에 있으면 안 된다. 한 턴에 두 플레이어가 서로 교차하는 경로를 가지는 것은 안 된다. 경로를 서로 교차하는 것이라는 것은 한 턴에 서로의 위치를 바꾸는 것을 의미한다.
#
# 예를 들어, A가 게임 판의 가장 왼쪽 위에 있고, B가 바로 오른쪽에 있다고 해보자. 만약, B가 왼쪽으로 움직인다면, A는 오른쪽으로 움직일 수 없다. 이때가 경로가 교차하는 것이다. 하지만, B가 왼쪽을 제외한 다른 방향으로 이동한다면, A는 오른쪽으로 이동할 수 있다.
#
# A가 (0, 0)에 있고, B가 (0, 1)에 있을 때, A가 오른쪽 아래방향 대각선으로 움직이고, B가 왼쪽 아래방향 대각선으로 움직일 때, (0.5, 0.5)에서 만나기는 하지만, 이것은 경로가 교차하는 것이 아니다.
#
# 입력
# 첫째 줄에 게임 판의 세로 크기 N과 가로 크기 M이 주어진다. N과 M은 20보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 게임 판의 상태가 주어진다. 빈 공간은 ., 벽은 X, A의 위치는 A, B의 위치는 B와 같이 표시된다.
#
# 출력
# 첫째 줄에 A와 B가 서로의 위치를 바꾸는데 드는 최소 턴을 출력한다. 만약 바꿀 수 없으면 -1을 출력한다.
from collections import deque
n, m = map(int, input().split())
grid = [list(str(input())) for _ in range(n)]
ay, ax = 0, 0
by, bx = 0, 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'A':
            ay, ax = i, j
            grid[i][j] = '.'
        if grid[i][j] == 'B':
            by, bx = i, j
            grid[i][j] = '.'
dy, dx = [-1, -1, 0, 1, 1, 1, 0, -1, 0], [0, 1, 1, 1, 0, -1, -1, -1, 0]
def move_A_and_B():
    q = deque()
    q.append((ay, ax, by, bx, 0))
    visited = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
    visited[ay][ax][by][bx] = True
    while q:
        cay, cax, cby, cbx, cnt = q.popleft()
        if (cay, cax, cby, cbx) == (by, bx, ay, ax):
            return cnt
        for i in range(9):
            nay, nax = cay+dy[i], cax+dx[i]
            if not (0 <= nay < n and 0 <= nax < m and grid[nay][nax] == '.'):
                continue
            for j in range(9):
                nby, nbx = cby+dy[j], cbx+dx[j]
                if not (0 <= nby < n and 0 <= nbx < m and grid[nby][nbx] == '.'):
                    continue
                if ((nay, nax) == (cby, cbx)) and ((nby, nbx) == (cay, cax)):
                    continue
                if (nay, nax) == (nby, nbx):
                    continue
                if not visited[nay][nax][nby][nbx]:
                    visited[nay][nax][nby][nbx] = True
                    q.append((nay, nax, nby, nbx, cnt+1))
    return -1
print(move_A_and_B())
