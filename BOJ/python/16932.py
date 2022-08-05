# 문제
# N×M인 배열에서 모양을 찾으려고 한다. 배열의 각 칸에는 0과 1 중의 하나가 들어있다. 두 칸이 서로 변을 공유할때, 두 칸을 인접하다고 한다.
#
# 1이 들어 있는 인접한 칸끼리 연결했을 때, 각각의 연결 요소를 모양이라고 부르자. 모양의 크기는 모양에 포함되어 있는 1의 개수이다.
#
# 배열의 칸 하나에 들어있는 수를 변경해서 만들 수 있는 모양의 최대 크기를 구해보자.
#
# 입력
# 첫째 줄에 배열의 크기 N과 M이 주어진다. 둘째 줄부터 N개의 줄에는 배열에 들어있는 수가 주어진다.
#
# 출력
# 첫째 줄에 수 하나를 변경해서 만들 수 있는 모양의 최대 크기를 출력한다.
#
# 제한
# 2 ≤ N, M ≤ 1,000
# 0과 1의 개수는 하나 이상이다.
from collections import deque
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
zeros = []
ones = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            zeros.append((i, j))
        if grid[i][j] == 1:
            ones.append((i, j))
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
visited = [[False for _ in range(m)] for _ in range(n)]
answer = 0
num = 1
groups = [0 for _ in range(n*m+1)]
def find_group(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    path = [(y, x)]
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                path.append((ny, nx))
                q.append((ny, nx))
    for y, x in path:
        grid[y][x] = num
    groups[num] = len(path)
for y, x in ones:
    if not visited[y][x]:
        find_group(y, x)
        num += 1
for y, x in zeros:
    result = 1
    near = []
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if grid[ny][nx] not in set(near):
                near.append(grid[ny][nx])
                result += groups[grid[ny][nx]]
    answer = max(answer, result)
print(answer)
