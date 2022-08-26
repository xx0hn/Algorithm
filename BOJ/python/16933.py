# 문제
# N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다. 이동하지 않고 같은 칸에 머물러있는 경우도 가능하다. 이 경우도 방문한 칸의 개수가 하나 늘어나는 것으로 생각해야 한다.
#
# 이번 문제에서는 낮과 밤이 번갈아가면서 등장한다. 가장 처음에 이동할 때는 낮이고, 한 번 이동할 때마다 낮과 밤이 바뀌게 된다. 이동하지 않고 같은 칸에 머무르는 경우에도 낮과 밤이 바뀌게 된다.
#
# 만약에 이동하는 도중에 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 K개 까지 부수고 이동하여도 된다. 단, 벽은 낮에만 부술 수 있다.
#
# 한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.
#
# 맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000), K(1 ≤ K ≤ 10)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.
#
# 출력
# 첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.
from collections import deque
n, m, k = map(int, input().split())
grid = [list(str(input())) for _ in range(n)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
# 1: 낮, -1: 밤
def move():
    q = deque()
    q.append((0, 0, 1, 0))
    visited = [[[0 for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
    visited[0][0] = [1 for _ in range(k+1)]
    time = 1
    while q:
        for _ in range(len(q)):
            y, x, dist, cnt = q.popleft()
            if (y, x) == (n-1, m-1):
                return dist
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx][cnt]:
                    if grid[ny][nx] == '0':
                        visited[ny][nx][cnt] = dist+1
                        q.append((ny, nx, dist+1, cnt))
                    elif grid[ny][nx] == '1':
                        if cnt+1 <= k and not visited[ny][nx][cnt+1]:
                            if time == 1:
                                visited[ny][nx][cnt+1] = dist+1
                                q.append((ny, nx, dist+1, cnt+1))
                            else:
                                q.append((y, x, dist+1, cnt))
        time *= (-1)
    return -1
print(move())
