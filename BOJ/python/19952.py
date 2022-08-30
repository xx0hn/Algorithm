# 문제
# 인성이는 인싸가 되기 위해서 인싸트 특별과정에 참가했다. 훈련 첫날 인성이는 험난한 미로에서 목적지에 도달해야 하는 훈련을 받고 있다. 제한 시간 안에 미로를 통과하지 못하면 명기 교관 님에게 욕을 듣기에 인성이는 최선을 다해 미로를 통과하려고 한다.
#
# 미로는 가로 길이 W, 세로 길이 H의 격자 형태를 가지며, 인성이는 한 번에 격자 상의 상, 하, 좌, 우로 한칸 씩 움직일 수 있다.  매 이동이 완료될 시에 인성이의 남은 힘은 1씩 감소하고, 남은 힘이 0이하인 경우에는 더 이상 움직이지 못하게 된다.
#
# 미로의 각 격자에는 장애물이 있는데, 각각의 장애물은 높이 정보를 가지고 있다. 장애물이 없는 위치는 전부 높이가 0 이다. 인성이가 이동할 때, 현재 위치보다 이동할 위치의 높이가 더 낮으면 아무런 제약을 갖지 않고 이동할 수 있다. 더 높은 곳으로 이동할 때는 점프를 할 수 있는데, 점프해야 하는 높이는 (이동할 곳의 높이 - 현재 위치한 곳의 높이) 이다. 이때 남아있는 힘이 점프해야 하는 높이보다 크거나 같으면 이동할 수 있고, 그렇지 않으면 이동하지 못한다.
#
# 인성이는 신체적 한계를 극복하고 무사히 목적지에 도달해서 명기 교관님의 욕설을 듣지 않을 수 있을까?
#
# 입력
# 첫째 줄에 테스트 케이스 T가 주어진다. 각 테스트 케이스는 다음과 같이 주어진다.
#
# 첫째 줄에 미로의 세로길이 H, 가로길이 W, 장애물의 개수 O, 초기 힘 F, 출발지의 좌표 정보 Xs(행), Ys(열)목적지의 좌표정보 Xe(행), Ye(열) 가 주어진다.
#
# 둘째 줄부터 O개의 줄에 장애물의 좌표 정보 X(행), Y(열) 와 높이 정보 L이 주어진다. 모든 장애물은 서로 다른 위치에 존재한다.
#
# 출력
# T개의 줄에 인성이가 목적지에 도착할 수 있을 때 "잘했어!!", 목적지에 도착할 수 없을 때 "인성 문제있어??" 를 출력한다.
from collections import deque
t = int(input())
def move_maze():
    q = deque()
    q.append((sy, sx, f))
    visited = [[False for _ in range(w)] for _ in range(h)]
    visited[sy][sx] = True
    dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
    while q:
        y, x, cur = q.popleft()
        if cur < 0:
            continue
        if (y, x) == (ey, ex):
            return True
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx]:
                if grid[ny][nx] <= grid[y][x]:
                    visited[ny][nx] = True
                    q.append((ny, nx, cur-1))
                else:
                    if grid[ny][nx] - grid[y][x] <= cur:
                        visited[ny][nx] = True
                        q.append((ny, nx, cur-1))
    return False
for _ in range(t):
    h, w, o, f, sy, sx, ey, ex = map(int, input().split())
    sy, sx, ey, ex = sy-1, sx-1, ey-1, ex-1
    grid = [[0 for _ in range(w)] for _ in range(h)]
    for _ in range(o):
        oy, ox, ol = map(int, input().split())
        grid[oy-1][ox-1] = ol
    if move_maze():
        print("잘했어!!")
    else:
        print("인성 문제있어??")
