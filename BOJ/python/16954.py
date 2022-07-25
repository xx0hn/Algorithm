# 문제
# 욱제는 학교 숙제로 크기가 8×8인 체스판에서 탈출하는 게임을 만들었다. 체스판의 모든 칸은 빈 칸 또는 벽 중 하나이다. 욱제의 캐릭터는 가장 왼쪽 아랫 칸에 있고, 이 캐릭터는 가장 오른쪽 윗 칸으로 이동해야 한다.
#
# 이 게임의 특징은 벽이 움직인다는 점이다. 1초마다 모든 벽이 아래에 있는 행으로 한 칸씩 내려가고, 가장 아래에 있어서 아래에 행이 없다면 벽이 사라지게 된다. 욱제의 캐릭터는 1초에 인접한 한 칸 또는 대각선 방향으로 인접한 한 칸으로 이동하거나, 현재 위치에 서 있을 수 있다. 이동할 때는 빈 칸으로만 이동할 수 있다.
#
# 1초 동안 욱제의 캐릭터가 먼저 이동하고, 그 다음 벽이 이동한다. 벽이 캐릭터가 있는 칸으로 이동하면 더 이상 캐릭터는 이동할 수 없다.
#
# 욱제의 캐릭터가 가장 오른쪽 윗 칸으로 이동할 수 있는지 없는지 구해보자.
#
# 입력
# 8개 줄에 걸쳐서 체스판의 상태가 주어진다. '.'은 빈 칸, '#'는 벽이다. 가장 왼쪽 아랫칸은 항상 벽이 아니다.
#
# 출력
# 욱제의 캐릭터가 가장 오른쪽 윗 칸에 도착할 수 있으면 1, 없으면 0을 출력한다.
from collections import deque
grid = [list(str(input())) for _ in range(8)]
wy, wx = 7, 0
ey, ex = 0, 7
dy, dx = [0, -1, -1, 0, 1, 1, 1, 0, -1], [0, 0, 1, 1, 1, 0, -1, -1, -1]
walls = []
for i in range(8):
    for j in range(8):
        if grid[i][j] == '#':
            walls.append((i, j))
def drop_walls():
    global walls
    new_walls = []
    for y, x in walls:
        if y < 7:
            new_walls.append((y+1, x))
    walls = new_walls[:]
def bfs():
    q = deque()
    q.append((7, 0))
    visited = [[False for _ in range(8)] for _ in range(8)]
    while q:
        for _ in range(len(q)):
            y, x = q.popleft()
            if (y, x) in set(walls):
                continue
            if (y, x) == (ey, ex):
                return True
            for i in range(9):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < 8 and 0 <= nx < 8 and not visited[ny][nx] and (ny, nx) not in set(walls):
                    visited[ny][nx] = True
                    q.append((ny, nx))
        if walls:
            visited = [[False for _ in range(8)] for _ in range(8)]
        drop_walls()
if bfs():
    print(1)
else:
    print(0)
