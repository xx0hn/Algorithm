# 문제
# 산으로 둘러싸인 고리분지에 사는 아기돼지 삼형제는 엄마돼지로부터 독립하여 새 집을 지으려 합니다.
#
# 고리분지는 N × M 크기의 2차원 격자로 나타낼 수 있고 각 칸의 지형은 초원, 빙판, 산 중 하나입니다.
#
# 고리분지에는 돼지가족들 뿐만 아니라 늑대들도 살고 있습니다. 늑대는 상하좌우 인접한 칸 중 산이 아닌 칸으로 이동할 수 있습니다. 만약 이동한 칸이 빙판이라면 초원을 밟거나 산에 부딪칠 때까지 이동한 방향으로 미끄러집니다. 산에 부딪친 경우 늑대는 빙판 위에 가만히 서있을 수 있고 다시 다른 방향으로 이동할 수 있습니다.
#
# 게으른 아기돼지들은 지푸라기로 집을 지을 예정이기 때문에 늑대가 집이 있는 칸에 도착하기만 한다면 손쉽게 침입할 수 있습니다. 고리분지에 사는 늑대들이 도달할 수 없고 지형이 초원인 칸을 '안전한 곳'이라고 부릅니다. 게으른 아기돼지들을 위해 고리분지의 지도가 주어지면 지도 위에 모든 안전한 곳의 위치를 표시해주세요.
#
# 입력
# 첫 번째 줄에는 격자의 행의 수를 나타내는 N (3 ≤ N ≤ 100) 과 격자의 열의 수를 나타내는 M (3 ≤ M ≤ 100) 이 주어집니다.
#
# 두 번째 줄부터 N개의 줄에 지도의 정보를 나타내는 길이가 M인 문자열들이 주어집니다.
#
# i+1번째 줄의 j번째 문자는 i번째 행 j번째 열의 지형 종류를 의미하며 '.' 일 경우 초원, '+' 일 경우 빙판, '#' 일 경우 산, 그리고 'W'는 늑대가 살고 있음을 나타냅니다. 늑대가 사는 칸은 여러 개일 수 있고 늑대가 사는 지형은 항상 초원입니다. 지도의 첫 번째, N번째 행과 첫 번째, M번째 열은 항상 산입니다.
#
# 출력
# 입력으로 주어진 지도를 출력하되 아기돼지가 살 수 있는 초원은 문자 'P'로 대체하여 출력합니다.
from collections import deque
n, m = map(int, input().split())
grid = [list(str(input())) for _ in range(n)]
wolf = deque()
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'W':
            wolf.append((i, j))
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
def move_wolf():
    visited = [[[0 for _ in range(4)] for _ in range(m)] for _ in range(n)]
    while wolf:
        y, x = wolf.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx][i]:
                if grid[ny][nx] == '.':
                    visited[ny][nx][i] = 1
                    wolf.append((ny, nx))
                elif grid[ny][nx] == '+':
                    while 0 <= ny < n and 0 <= nx < m and grid[ny][nx] == '+':
                        visited[ny][nx][i] = 1
                        ny, nx = ny+dy[i], nx+dx[i]
                    if not (0 <= ny < n and 0 <= nx < m) or grid[ny][nx] == '#':
                        ny, nx = ny-dy[i], nx-dx[i]
                    else:
                        visited[ny][nx][i] = 1
                    wolf.append((ny, nx))
    return visited
result = move_wolf()
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.' and max(result[i][j]) == 0:
            grid[i][j] = 'P'
for i in range(n):
    print(''.join(grid[i]))
