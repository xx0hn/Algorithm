# 문제
# 캐슬 디펜스는 성을 향해 몰려오는 적을 잡는 턴 방식의 게임이다. 게임이 진행되는 곳은 크기가 N×M인 격자판으로 나타낼 수 있다. 격자판은 1×1 크기의 칸으로 나누어져 있고, 각 칸에 포함된 적의 수는 최대 하나이다. 격자판의 N번행의 바로 아래(N+1번 행)의 모든 칸에는 성이 있다.
#
# 성을 적에게서 지키기 위해 궁수 3명을 배치하려고 한다. 궁수는 성이 있는 칸에 배치할 수 있고, 하나의 칸에는 최대 1명의 궁수만 있을 수 있다. 각각의 턴마다 궁수는 적 하나를 공격할 수 있고, 모든 궁수는 동시에 공격한다. 궁수가 공격하는 적은 거리가 D이하인 적 중에서 가장 가까운 적이고, 그러한 적이 여럿일 경우에는 가장 왼쪽에 있는 적을 공격한다. 같은 적이 여러 궁수에게 공격당할 수 있다. 공격받은 적은 게임에서 제외된다. 궁수의 공격이 끝나면, 적이 이동한다. 적은 아래로 한 칸 이동하며, 성이 있는 칸으로 이동한 경우에는 게임에서 제외된다. 모든 적이 격자판에서 제외되면 게임이 끝난다.
#
# 게임 설명에서 보다시피 궁수를 배치한 이후의 게임 진행은 정해져있다. 따라서, 이 게임은 궁수의 위치가 중요하다. 격자판의 상태가 주어졌을 때, 궁수의 공격으로 제거할 수 있는 적의 최대 수를 계산해보자.
#
# 격자판의 두 위치 (r1, c1), (r2, c2)의 거리는 |r1-r2| + |c1-c2|이다.
#
# 입력
# 첫째 줄에 격자판 행의 수 N, 열의 수 M, 궁수의 공격 거리 제한 D가 주어진다. 둘째 줄부터 N개의 줄에는 격자판의 상태가 주어진다. 0은 빈 칸, 1은 적이 있는 칸이다.
#
# 출력
# 첫째 줄에 궁수의 공격으로 제거할 수 있는 적의 최대 수를 출력한다.
#
# 제한
# 3 ≤ N, M ≤ 15
# 1 ≤ D ≤ 10
import copy
from collections import deque
n, m, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
answer = 0
arrows = []
def get_arrows(cur, arrow):
    if cur == m:
        if len(arrow) == 3:
            arrows.append(arrow)
        return
    if len(arrow) > 3:
        return
    get_arrows(cur+1, arrow+[(n, cur)])
    get_arrows(cur+1, arrow)
def move_enemy():
    global tmp_grid
    result = [[0 for _ in range(m)]]
    for i in range(n-1):
        result.append(tmp_grid[i])
    tmp_grid = copy.deepcopy(result)
def find_attackable(arrow, grid):
    y, x = arrow
    q = deque()
    q.append((y, x, 1))
    visited = [[False for _ in range(m)] for _ in range(n)]
    results = []
    while q:
        y, x, dist = q.popleft()
        if dist > d:
            continue
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx, dist+1))
                if grid[ny][nx] == 1:
                    results.append((ny, nx, dist+1))
    if not results:
        return (-1, -1)
    results.sort(key=lambda x:(x[2], x[1], x[0]))
    return (results[0][0], results[0][1])
get_arrows(0, [])
for i in range(len(arrows)):
    tmp_ans = 0
    tmp_grid = copy.deepcopy(grid)
    while tmp_grid != [[0 for _ in range(m)] for _ in range(n)]:
        rmv = set()
        for j in range(3):
            rmv.add(find_attackable(arrows[i][j], tmp_grid))
        for ry, rx in rmv:
            if (ry, rx) == (-1, -1):
                continue
            tmp_grid[ry][rx] = 0
            tmp_ans += 1
        move_enemy()
    answer = max(answer, tmp_ans)
print(answer)
