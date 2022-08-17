# 문제
# 늑대 현우는 피에 굶주린 사냥꾼들에게 벗어나려고 도망치고 있다. 사냥꾼은 매우 똑똑해서 나무 뒤에 숨어있다. 현우도 이 사실을 알고있다. 하지만, 어떤 나무 뒤에 사냥꾼들이 숨어있는지 알지 못한다. 현우는 사냥꾼에게 잡히지 않기 위해서 숲의 한 오두막으로 대피하려고 한다. 현우는 나무와 거리가 최대한 떨어지는 경로로 대피하려고 한다.
#
# 숲은 N×M 크기의 그리드로 나타낼 수 있다. 각 칸이 빈 목초지라면 '.', 나무가 있다면 '+', 현재 현우의 위치는 'V', 오두막의 위치는 'J'로 나타나있다. 현우는 현재 있는 위치에서 동서남북으로 인접한 칸으로 이동할 수 있고, 나무가 있는 칸으로도 이동할 수 있다.
#
# 만약 현우가 지금 R행 C열에 있고, 나무가 A행 B열에 있다면, 현우와 나무의 거리는 |R-A| + |C-B|이다.
#
# 현우는 오두막으로 도망치는 가장 안전한 길로 이동하려고 한다. 가장 안전한 길이란 현우가 이동하는 모든 칸에서 나무와 거리의 최솟값이 가장 큰 경로이다. 또, 오두막이 있는 칸도 경로의 일부이기 때문에 나무와 거리를 계산해야 한다.
#
# 숲의 지도가 주어졌을 때, 가장 안전한 길을 찾는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N과 M (1 ≤ N, M ≤ 500)이 주어진다. 둘째 줄부터 N개 줄에는 숲의 지도가 주어진다. 지도에 'V'와 'J'는 딱 하나만 있고, 적어도 하나의 '+'가 있다.
#
# 출력
# 첫째 줄에 가장 안전한 경로에서 나무와 현우와 거리의 최솟값을 출력한다.
import heapq
from collections import deque
n, m = map(int, input().split())
grid = [list(str(input())) for _ in range(n)]
sy, sx = 0, 0
trees = deque()
trees_dists = [[-1 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'V':
            sy, sx = i, j
        if grid[i][j] == '+':
            trees.append((i, j, 0))
            trees_dists[i][j] = 0
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
def between_tree_and_me():
    while trees:
        y, x, dist = trees.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < m and trees_dists[ny][nx] == -1:
                trees_dists[ny][nx] = dist+1
                trees.append((ny, nx, dist+1))
def go_to_J():
    q = []
    heapq.heappush(q, (-trees_dists[sy][sx], sy, sx))
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[sy][sx] = True
    result = 1e9
    while q:
        td, y, x = heapq.heappop(q)
        result = min(result, -td)
        if grid[y][x] == 'J':
            return result
        td *= -1
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                visited[ny][nx] = True
                heapq.heappush(q, (-trees_dists[ny][nx], ny, nx))
between_tree_and_me()
print(go_to_J())
