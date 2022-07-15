# 문제
# 인체에 치명적인 바이러스를 연구하던 연구소에 승원이가 침입했고, 바이러스를 유출하려고 한다. 승원이는 연구소의 특정 위치에 바이러스 M개를 놓을 것이고, 승원이의 신호와 동시에 바이러스는 퍼지게 된다.
#
# 연구소는 크기가 N×N인 정사각형으로 나타낼 수 있으며, 정사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.
#
# 일부 빈 칸은 바이러스를 놓을 수 있는 칸이다. 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제되며, 1초가 걸린다.
#
# 예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자. 0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 칸이다.
#
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 2 0 1 1
# 0 1 0 0 0 0 0
# 2 1 0 0 0 0 2
# M = 3이고, 바이러스를 아래와 같이 놓은 경우 6초면 모든 칸에 바이러스를 퍼뜨릴 수 있다. 벽은 -, 바이러스를 놓은 위치는 0, 빈 칸은 바이러스가 퍼지는 시간으로 표시했다.
#
# 6 6 5 4 - - 2
# 5 6 - 3 - 0 1
# 4 - - 2 - 1 2
# 3 - 2 1 2 2 3
# 2 2 1 0 1 - -
# 1 - 2 1 2 3 4
# 0 - 3 2 3 4 5
# 시간이 최소가 되는 방법은 아래와 같고, 5초만에 모든 칸에 바이러스를 퍼뜨릴 수 있다.
#
# 0 1 2 3 - - 2
# 1 2 - 3 - 0 1
# 2 - - 2 - 1 2
# 3 - 2 1 2 2 3
# 3 2 1 0 1 - -
# 4 - 2 1 2 3 4
# 5 - 3 2 3 4 5
# 연구소의 상태가 주어졌을 때, 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간을 구해보자.
#
# 입력
# 첫째 줄에 연구소의 크기 N(5 ≤ N ≤ 50), 놓을 수 있는 바이러스의 개수 M(1 ≤ M ≤ 10)이 주어진다.
#
# 둘째 줄부터 N개의 줄에 연구소의 상태가 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 칸이다. 2의 개수는 M보다 크거나 같고, 10보다 작거나 같은 자연수이다.
#
# 출력
# 연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간을 출력한다. 바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1을 출력한다.
from collections import deque
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
virus_possible = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            virus_possible.append((i, j))
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
viruses = []
def get_viruses(cur, virus):
    if cur == len(virus_possible):
        if len(virus) == m:
            viruses.append(virus)
        return
    if len(virus) > m:
        return
    get_viruses(cur+1, virus+[virus_possible[cur]])
    get_viruses(cur+1, virus)
def spread_viruses(virus):
    q = deque()
    visited = [[1e9 for _ in range(n)] for _ in range(n)]
    result = 0
    for y, x in virus:
        visited[y][x] = 0
        q.append((y, x, 0))
    while q:
        y, x, time = q.popleft()
        if time > visited[y][x]:
            continue
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < n and grid[ny][nx] != 1 and visited[ny][nx] > visited[y][x]+1:
                q.append((ny, nx, time+1))
                visited[ny][nx] = min(time+1, visited[ny][nx])
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 1 and visited[i][j] != 1e9:
                result = max(result, visited[i][j])
            elif grid[i][j] != 1 and visited[i][j] == 1e9:
                result = 1e9
                return result
    return result
answer = 1e9
get_viruses(0, [])
for i in range(len(viruses)):
    answer = min(answer, spread_viruses(viruses[i]))
if answer == 1e9:
    answer = -1
print(answer)
