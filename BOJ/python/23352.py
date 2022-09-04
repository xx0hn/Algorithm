# 문제
# 여러 방들로 둘러싸인 구역을 탈출해야 한다. 알맞은 비밀번호를 입력하면 탈출할 수 있다.
#
# 구역의 지도는 $N \times M$ 크기의 격자판으로 나타낼 수 있으며 각 칸은 방을 의미하고 각 칸에는 0부터 9까지의 숫자가 적혀있는데 이는 해당하는 방에 적힌 숫자를 의미한다.
#
# 상하좌우 4가지 방향으로만 움직일 수 있으며, 0이 적힌 방은 들어갈 수 없다.
#
# 비밀번호의 힌트는 다음과 같다.
#
# 임의의 방에서 다른 방으로 이동할 때는 항상 두 방 사이의 최단 경로로 이동한다.
# 1번을 만족하는 경로 중 가장 긴 경로의 시작 방과 끝 방에 적힌 숫자의 합
# 만약 위 2가지 조건을 만족하는 경로가 여러 개라면, 시작 방과 끝 방에 적힌 숫자의 합이 가장 큰 값이 비밀번호가 된다.
#
# 시작 방과 끝 방은 동일한 위치일 수도 있다.
#
# <예시> $5 \times 5$ 형태의 지도가 주어질 때, 위의 2가지 조건을 만족하는 경로는 다음과 같다.
#
#
#
# 이 때 비밀번호가 무엇인지를 구해라.
#
# 만약 비밀번호를 만들 수 없는 경우 0을 출력한다.
#
# 입력
# 첫줄에 지도의 세로 크기 $N$($1 \le N \le 50$), 가로 크기 $M$($1 \le M \le 50$)이 공백을 두고 주어진다.
#
# 둘째 줄부터 $N$줄에 걸쳐 각 방들의 정보 $A$($0 \le A \le 9$)가 공백을 두고 주어진다.
#
# 출력
# 올바른 비밀번호를 출력한다.
from collections import deque
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
answers = []
def bfs(sy, sx):
    q = deque()
    q.append((sy, sx, 0))
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[sy][sx] = True
    while q:
        y, x, cnt = q.popleft()
        flag = False
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] > 0 and not visited[ny][nx]:
                flag = True
                visited[ny][nx] = True
                q.append((ny, nx, cnt+1))
        if not flag:
            answers.append((cnt, grid[sy][sx]+grid[y][x]))
for i in range(n):
    for j in range(m):
        if grid[i][j] > 0:
            bfs(i, j)
answers.sort(key=lambda x:(x[0], x[1]), reverse=True)
print(answers[0][1])
