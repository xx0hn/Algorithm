# 문제
# 어제 선물을 모두 포장한 민식이는 이제 선물을 배달하려고 한다. 민식이가 선물을 배달할 곳은 이 문제를 읽는 사람들이 앉아 있는 교실이다. 교실은 직사각형모양이고, 모두 같은 크기의 정사각형 블록으로 나누어져 있다.
#
# 입력으로 교실의 지도가 주어진다. 각각의 정사각형 블록은 다음과 같이 4가지 종류가 있다.
#
# S: 지금 민식이가 있는 곳이다. 이곳이 민식이가 배달을 시작하는 곳이고 1개만 있다.
# C: 민식이가 반드시 선물을 배달해야 하는 곳이다. 이러한 블록은 정확하게 2개 있다.
# #: 민식이가 갈 수 없는 곳이다.
# .: 민식이가 자유롭게 지나갈 수 있는 곳이다.
# 민식이가 한 블록 동서남북으로 이동하는데는 1분이 걸린다. 민식이는 네가지 방향 중 하나로 이동할 수 있으며, 교실을 벗어날 수 없다. 민식이가 선물을 배달해야 하는 곳에 들어갈 때, 민식이는 그 곳에 있는 사람 모두에게 선물을 전달해야 한다. 이 상황은 동시에 일어나며, 추가적인 시간이 소요되지 않는다.
#
# 민식이는 어느 누구도 자신을 보지 않았으면 하기 때문에, 멈추지 않고 매 시간마다 방향을 바꿔야 한다. 이 말은 같은 방향으로 두 번 연속으로 이동할 수 없다는 말이다. 민식이가 선물을 모두 배달하는데 걸리는 시간의 최솟값을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 교실의 세로 크기 N과 가로 크기 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 교실의 지도가 주어진다.
#
# 출력
# 첫째 줄에 민식이가 선물을 모두 배달하는데 걸리는 시간의 최솟값을 출력한다. 만약 불가능 할 때는 -1을 출력한다.
from collections import deque
n, m = map(int, input().split())
grid = [list(str(input())) for _ in range(n)]
sy, sx = 0, 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S':
            sy, sx = i, j
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
def bfs():
    q = deque()
    visited = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]
    q.append((sy, sx, -1, 0))
    cnt = 0
    save_point = deque()
    while q:
        y, x, d, time = q.popleft()
        for i in range(4):
            if i == d:
                continue
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] != '#' and not visited[ny][nx][i]:
                if grid[ny][nx] == 'C':
                    if not save_point:
                        cnt += 1
                        if cnt == 2:
                            return time+1
                    elif save_point[0][0] != ny or save_point[0][1] != nx:
                        continue
                    save_point.append((ny, nx, i, time+1))
                else:
                    if save_point:
                        continue
                    visited[ny][nx][i] = True
                    q.append((ny, nx, i, time+1))
        if not q and save_point:
            visited = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]
            grid[save_point[0][0]][save_point[0][1]] = '.'
            while save_point:
                q.append(save_point.pop())
    return -1
print(bfs())
