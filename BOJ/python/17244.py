# 문제
#
#
# 경재씨는 저녁 약속을 가기 전 챙기지 않은 물건들이 있는 지 확인하고 있다. 필요한 물건은 전부 챙긴 것 같았고 외출 후 돌아오는 길에 경재씨는 외쳤다.
#
# "아 맞다 우산!!!"
#
# 경재 씨는 매번 외출하고 나서야 어떤 물건을 집에 놓고 왔다는 것을 떠올릴 때마다 자책감에 시달리는 것이 너무 싫었다.
#
# 외출이 잦은 경재 씨는 반복되는 일을 근절하기 위해 꼭 챙겨야 할 물건들을 정리해보았다. 하지만 지갑, 스마트폰, 우산, 차 키, 이어폰, 시계, 보조 배터리 등 종류와 개수가 너무 많았다.
#
# 평소 불필요한 움직임을 아주 싫어하는 경재 씨는 이 물건들을 최대한 빠르게 챙겨서 외출하는 이동 경로를 알고 싶었다.
#
# 경재 씨는 한 걸음에 상하좌우에 인접한 칸으로만 움직일 수 있다.
#
# 경재 씨를 위해 집을 위에서 바라본 모습과 챙겨야 할 물건들의 위치들을 알고 있을 때, 물건을 모두 챙겨서 외출하기까지 최소 몇 걸음이 필요한지 구하는 프로그램을 작성하자.
#
# 입력
# 첫 번째 줄에는 집의 가로 길이 N과 세로 길이 M이 입력된다. (3 ≤ N, M ≤ 50)
#
# 두 번째 줄부터는 집의 구조가 예제 입력과 같이 주어진다.
#
# 비어있는 곳은 '.'로 벽은 '#'로 입력된다. 경재 씨의 현재 위치는 S, 나가는 문의 위치는 E, 챙겨야 하는 물건은 종류에 상관없이 X로 입력된다.
#
# 챙겨야 하는 물건은 최대 5개까지 있을 수 있다. 집은 언제나 벽으로 둘러싸여 있고, 나가는 문은 언제나 하나이다.
#
# 출력
# S에서 출발하여 모든 물건을 챙겨서 E까지 도착할 수 있는 최소 시간을 출력한다. 모든 물건을 챙길 수 없는 경우는 주어지지 않는다.
from collections import deque
n, m = map(int, input().split())
grid = [list(str(input())) for _ in range(m)]
stuffs = []
sy, sx = 0, 0
num = 1
for i in range(m):
    for j in range(n):
        if grid[i][j] == 'S':
            sy, sx = i, j
        if grid[i][j] == 'X':
            stuffs.append((num, i, j))
            grid[i][j] = str(num)
            num += 1
visited = [[[False for _ in range(64)] for _ in range(n)] for _ in range(m)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
def ready_to_go():
    q = deque()
    q.append((sy, sx, 1, 0))
    visited[sy][sx][1] = True
    while q:
        y, x, cnt, time = q.popleft()
        if grid[y][x] == 'E' and cnt == (1 << num) - 1:
            return time
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < m and 0 <= nx < n and grid[ny][nx] != '#':
                if str(grid[ny][nx]).isdigit():
                    if cnt&(1 << int(grid[ny][nx])) != int(grid[ny][nx]):
                        if not visited[ny][nx][cnt|(1 << int(grid[ny][nx]))]:
                            visited[ny][nx][cnt|(1 << int(grid[ny][nx]))] = True
                            q.append((ny, nx, cnt|(1 << int(grid[ny][nx])), time+1))
                else:
                    if not visited[ny][nx][cnt]:
                        visited[ny][nx][cnt] = True
                        q.append((ny, nx, cnt, time+1))
    return -1
print(ready_to_go())
