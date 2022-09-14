# 문제
# 멤멤월드에서는 일정 주기마다 랜덤한 위치에서 보스몬스터가 소환된다.
#
# 이 보스몬스터의 전리품은 아주 좋아 모든 멤멤월드의 플레이어들은 소환 알림만을 기다린다고 한다. 전리품은 한 대라도 때렸다면 피해를 준 비율대로 지급된다고 한다.
#
# 현재 멤멤월드의 지도와 플레이어들의 정보, 보스몬스터의 체력이 주어졌을 때 최대 몇 명의 플레이어가 전리품을 가져갈 수 있는지 계산해보자.
#
# 단, 모든 플레이어는 보스몬스터가 소환되면 보스몬스터의 위치로 최대한 빠른 경로로 이동하며 이동한 경우 공격을 바로 시작한다. 공격에 소모되는 시간은 1초이며 보스와 같은 위치에 있는 모든 플레이어의 공격은 동시에 이뤄진다. 그리고 플레이어는 상, 하, 좌, 우로 이동할 수 있고 이동에 소요되는 시간은 1초이다. 또한 한 지점에 여러명의 플레이어가 위치할 수 있다.
#
# 입력
# 입력의 첫째 줄에는 멤멤월드의 지도의 크기를 나타내는 두 정수 M(6 ≤ M ≤ 1000), N(6 ≤ N ≤ 1000)과 플레이어의 수 P(1 ≤ P ≤ 26)가 주어진다. M은 지도의 세로 길이, N은 지도의 가로 길이이다.
#
# 입력의 둘째 줄부터 M개의 줄까지 지도의 정보가 주어진다. 이때 ‘.’은 이동할 수 있는 길, ‘X’는 이동할 수 없는길, 알파벳 소문자는 플레이어의 아이디이며 ‘B’는 보스몬스터의 위치이다.
#
# 그 다음 줄부터 P개의 줄까지 플레이어의 아이디와 dps(1 ≤ dps ≤ 10000)가 주어진다. 아이디는 영문 소문자이다. dps란 1초당 얼만큼의 보스몬스터의 체력을 줄일 수 있는지 의미한다. 그 다음 줄은 보스몬스터의 HP(10 ≤ HP ≤ 1000000)가 주어진다. dps와 HP는 정수이다.
#
# 아무 플레이어도 보스몬스터를 잡으러 갈 수 없는 경우의 입력은 주어지지 않는다.
#
# 출력
# 전리품을 가져갈 수 있는 플레이어의 수의 최댓값을 출력한다.
from collections import defaultdict, deque
m, n, p = map(int, input().split())
grid = [list(str(input())) for _ in range(m)]
location = defaultdict(tuple)
powers = defaultdict(int)
for i in range(m):
    for j in range(n):
        if grid[i][j] != 'B' and grid[i][j] != '.' and grid[i][j] != 'X':
            location[grid[i][j]] = (i, j)
for _ in range(p):
    a, b = map(str, input().split())
    powers[a] = int(b)
boss = int(input())
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
arrived_time = defaultdict(int)
def kill_boss(player):
    q = deque()
    py, px = location[player]
    q.append((py, px, 0))
    visited = [[False for _ in range(n)] for _ in range(m)]
    visited[py][px] = True
    while q:
        y, x, time = q.popleft()
        if grid[y][x] == 'B':
            arrived_time[player] = time
            break
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < m and 0 <= nx < n and grid[ny][nx] != 'X' and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx, time+1))
for key, _ in location.items():
    kill_boss(key)
cnt = set()
time = 0
while boss:
    for key, value in arrived_time.items():
        if value <= time:
            if key not in cnt:
                cnt.add(key)
            boss = max(0, boss-powers[key])
    time += 1
print(len(cnt))
