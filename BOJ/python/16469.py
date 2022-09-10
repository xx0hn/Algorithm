# 문제
# “OK 계획대로 되고 있어”
#
# 한국 힙합의 떠오르는 신성인 마미손은 악당 무리에게서 도망치고 있다. 악당 무리는 넉살, 스윙스, 창모 3명으로 이루어져 있다. 마미손은 도망치는 도중 R*C 크기의 미로를 만났고, 미로 안에 숨기로 했다. 뒤늦게 미로에 도착한 악당 무리는 마미손을 찾기 위해 뿔뿔이 흩어져 찾아보기로 했다. 이때 악당들은 항상 상하좌우로만 이동 가능하고, 이동 속도는 모두 같으며 칸 단위로만 이동 가능하다. 또한 악당들은 움직이지 않고 제자리에 멈춰있을 수도 있다. 넉살, 스윙스, 창모는 서로 다른 지점에서 마미손을 찾기 시작하는데 이들은 세 명이 한 지점에서 모였을 때 걸린 시간이 최소가 되는 지점에 마미손이 숨어있다고 확신한다. 마미손은 숨기 이전에 악당들이 어디서 탐색을 시작할지 알고 있어 악당들이 찾아올 지점들을 피해 숨으려고 한다.
#
# 힘든 모험을 시작한 마미손. 이 모험에서 주인공은 절대 죽지 않는다는 것을 여러분이 마미손이 되어 보여주자! R*C 크기의 미로가 주어지고, 넉살, 스윙스, 창모의 시작 위치가 주어질 때, 한 지점에 세 악당이 모일 때 걸린 시간이 최소가 되는 지점을 마미손에게 알려주자.
#
# 입력
# 첫째 줄에 미로의 행과 열의 크기를 나타내는 자연수 R과 C가 주어진다. (2 ≤ R, C ≤ 100) 다음 R줄에 걸 쳐 길이 C로 이루어진 각 줄의 미로의 정보가 공백 없이 주어진다. 숫자 0은 이동 가능한 길, 1은 벽을 나타낸다. 그 다음 줄부터 3개의 줄은 각각 넉살, 스윙스 창모의 위치(행, 열)를 나타내는 자연수 Xi, Yi가 (1 ≤ Xi ≤ R, 1 ≤ Yi ≤ C)주어진다. 악당들은 위치가 겹치지 않고, 항상 이동 가능한 길에서 출발한다. 맨 왼쪽 위의 위치는 (1, 1)이다.
#
# 출력
# 첫째 줄에 한 지점에 세 악당이 모일 때 걸린 시간의 최소 값을 출력한다. 둘째 줄에는 그러한 지점의 개수를 출력한다. 만약 세 악당이 모일 수 있는 지점이 존재하지 않는다면 -1를 출력한다.
from collections import deque
r, c = map(int, input().split())
grid = [list(str(input())) for _ in range(r)]
villain = [list(map(int, input().split())) for _ in range(3)]
dists = [[[1e9 for _ in range(3)] for _ in range(c)] for _ in range(r)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
def bfs(idx, sy, sx):
    q = deque()
    q.append((sy-1, sx-1, 0))
    dists[sy-1][sx-1][idx] = 0
    while q:
        y, x, dist = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < r and 0 <= nx < c and grid[ny][nx] == '0' and dists[ny][nx][idx] == 1e9:
                dists[ny][nx][idx] = dist+1
                q.append((ny, nx, dist+1))
for idx in range(3):
    bfs(idx, villain[idx][0], villain[idx][1])
answer = 1e9
cnt = 0
for i in range(r):
    for j in range(c):
        if dists[i][j][0] == 1e9 or dists[i][j][1] == 1e9 or dists[i][j][2] == 1e9:
            continue
        ans = max(dists[i][j])
        if answer > ans:
            answer = ans
            cnt = 1
        elif answer == ans:
            cnt += 1
if answer == 1e9:
    print(-1)
else:
    print(answer)
    print(cnt)
