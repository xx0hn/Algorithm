# 문제
# CTP의 대표 상남자 영조는 자유롭게 이동하는 것을 좋아한다. 그렇지만 영조는 상남자이기 때문에 위아래로만 간다. 따라서 위, 아래로는 얼마든지 이동할 수 있지만 왼쪽, 오른쪽으로는 이동하지 않는다. 하지만 영조의 행동이 답답한 영조의 친구 보성이는 영조가 위, 아래로만 가는 걸 막기 위해 영조와 같이 다니며 왼쪽으로 최대 L번 오른쪽으로 최대 R번만큼 이동할 수 있게 영조를 도와준다. 영조와 보성이는 지도 밖으로는 나가지 않는다.
#
# 갈수 있는 땅, 벽의 위치, 영조와 보성이의 출발 위치가 지도 정보로 주어졌을 때 영조와 보성이가 출발 위치로부터 이동해서 갈 수 있는 모든 땅의 개수를 구해보자.
#
# 다음은 이해를 돕기 위한 예제1 그림이다.
#
#
#
# 영조와 보성이가 시작 위치에서 갈수 있는 땅은 파란색, 벽이 있어 갈수 없는 땅은 검은색이다.
#
# 다음 그림은 영조와 보성이가 시작 위치에서 왼쪽으로 한 칸 이동했을 때이다.
#
#
#
# 왼쪽으로 한 칸 이동하였으므로 더 이상 왼쪽으로는 갈 수 없고, 현재 상태에서 갈수 있는 길은 파란색으로 나타내었다.
#
# 다음 그림은 영조와 보성이가 시작 위치에서 아래로 갔을 때이다.
#
#
#
# 영조와 보성이가 아래로 한 칸 이동했을 때의 갈 수 있는 땅과 현재 상태이다.
#
# 다음 그림은 영조와 보성이가 자유롭게 이동하였을 때 도달 가능한 땅을 나타낸다.
#
#
#
# 영조와 보성이가 최대 왼쪽으로 L번, 오른쪽으로 R번 만큼 움직여서 자유롭게 이동했을 때 도달 가능한 땅은 13칸이다.
#
# 입력
# 첫 번째 줄에 지도의 행과 열 N, M이 주어진다 (1 ≤ N, M ≤ 1,000)
#
# 두 번째 줄에 왼쪽과 오른쪽으로 갈수 있는 최대 횟수 L, R이 주어진다. (0 ≤ L, R ≤ M)
#
# 세 번째 줄부터 N+2줄까지 M 의 크기만큼 지도가 주어진다.
#
# 0: 갈 수 있는 땅
# 1: 벽이 있어 갈 수 없는 땅
# 2: 영조와 보성이가 있는 위치
# 출력
# 시작 위치를 포함하여 갈수 있는 땅의 개수를 출력한다.
from collections import deque
n, m = map(int, input().split())
l, r = map(int, input().split())
grid = [list(str(input())) for _ in range(n)]
sy, sx = 0, 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '2':
            sy, sx = i, j
            grid[i][j] = '0'
            break
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[False for _ in range(m)] for _ in range(n)]
def real_man():
    q = deque()
    q.append((sy, sx, l, r))
    visited[sy][sx] = True
    result = 1
    while q:
        y, x, l_cnt, r_cnt = q.popleft()
        for i in range(2):
            ny, nx = y+dy[i], x+dx[i]
            while 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and grid[ny][nx] == '0':
                visited[ny][nx] = True
                result += 1
                q.append((ny, nx, l_cnt, r_cnt))
                ny, nx = ny+dy[i], nx+dx[i]
        if l_cnt > 0:
            ny, nx = y+dy[2], x+dx[2]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and grid[ny][nx] == '0':
                visited[ny][nx] = True
                result += 1
                q.append((ny, nx, l_cnt-1, r_cnt))
        if r_cnt > 0:
            ny, nx = y+dy[3], x+dx[3]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and grid[ny][nx] == '0':
                visited[ny][nx] = True
                result += 1
                q.append((ny, nx, l_cnt, r_cnt-1))
    return result
print(real_man())
