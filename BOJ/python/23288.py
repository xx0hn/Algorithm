# 문제
# 크기가 N×M인 지도가 존재한다. 지도의 오른쪽은 동쪽, 위쪽은 북쪽이다. 지도의 좌표는 (r, c)로 나타내며, r는 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로부터 떨어진 칸의 개수이다. 가장 왼쪽 위에 있는 칸의 좌표는 (1, 1)이고, 가장 오른쪽 아래에 있는 칸의 좌표는 (N, M)이다. 이 지도의 위에 주사위가 하나 놓여져 있으며, 주사위의 각 면에는 1보다 크거나 같고, 6보다 작거나 같은 정수가 하나씩 있다. 주사위 한 면의 크기와 지도 한 칸의 크기는 같고, 주사위의 전개도는 아래와 같다.
#
#   2
# 4 1 3
#   5
#   6
# 주사위는 지도 위에 윗 면이 1이고, 동쪽을 바라보는 방향이 3인 상태로 놓여져 있으며, 놓여져 있는 곳의 좌표는 (1, 1) 이다. 지도의 각 칸에도 정수가 하나씩 있다. 가장 처음에 주사위의 이동 방향은 동쪽이다. 주사위의 이동 한 번은 다음과 같은 방식으로 이루어진다.
#
# 주사위가 이동 방향으로 한 칸 굴러간다. 만약, 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다.
# 주사위가 도착한 칸 (x, y)에 대한 점수를 획득한다.
# 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸 (x, y)에 있는 정수 B를 비교해 이동 방향을 결정한다.
# A > B인 경우 이동 방향을 90도 시계 방향으로 회전시킨다.
# A < B인 경우 이동 방향을 90도 반시계 방향으로 회전시킨다.
# A = B인 경우 이동 방향에 변화는 없다.
# 칸 (x, y)에 대한 점수는 다음과 같이 구할 수 있다. (x, y)에 있는 정수를 B라고 했을때, (x, y)에서 동서남북 방향으로 연속해서 이동할 수 있는 칸의 수 C를 모두 구한다. 이때 이동할 수 있는 칸에는 모두 정수 B가 있어야 한다. 여기서 점수는 B와 C를 곱한 값이다.
#
# 보드의 크기와 각 칸에 있는 정수, 주사위의 이동 횟수 K가 주어졌을때, 각 이동에서 획득하는 점수의 합을 구해보자.
#
# 이 문제의 예제 1부터 7은 같은 지도에서 이동하는 횟수만 증가시키는 방식으로 구성되어 있다. 예제 8은 같은 지도에서 이동하는 횟수를 매우 크게 만들었다.
#
# 입력
# 첫째 줄에 지도의 세로 크기 N, 가로 크기 M (2 ≤ N, M ≤ 20), 그리고 이동하는 횟수 K (1 ≤ K ≤ 1,000)가 주어진다.
#
# 둘째 줄부터 N개의 줄에 지도에 쓰여 있는 수가 북쪽부터 남쪽으로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다. 지도의 각 칸에 쓰여 있는 수는 10 미만의 자연수이다.
#
# 출력
# 첫째 줄에 각 이동에서 획득하는 점수의 합을 출력한다.
from collections import deque
n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
top, front, right = 1, 5, 3 # 양면의 합은 7
dy, dx = [0, -1, 0, 1], [1, 0, -1, 0] # 동 북 서 남
def get_point(y, x):
    q = deque()
    q.append((y, x))
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[y][x] = True
    point = grid[y][x]
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] == grid[y][x] and not visited[ny][nx]:
                visited[ny][nx] = True
                point += grid[ny][nx]
                q.append((ny, nx))
    return point
def move_dice(y, x, d):
    global top, front, right, cur, cur_d
    ny, nx = y+dy[d], x+dx[d]
    if not (0 <= ny < n and 0 <= nx < m):
        d = (d+2)%4
        cur_d = d
        ny, nx = y+dy[d], x+dx[d]
    if d == 0:
        top, front, right = 7-right, front, top
    elif d == 1:
        top, front, right = front, 7-top, right
    elif d == 2:
        top, front, right = right, front, 7-top
    elif d == 3:
        top, front, right = 7-front, top, right
    cur = [ny, nx]
def find_dir(i, y, x, d, bottom):
    if i == 0:
        return 0
    if bottom > grid[y][x]:
        return (d+3)%4
    elif bottom < grid[y][x]:
        return (d+1)%4
    else:
        return d
cur = [0, 0]
cur_d = 0
answer = 0
for i in range(k):
    cur_d = find_dir(i, cur[0], cur[1], cur_d, 7-top)
    move_dice(cur[0], cur[1], cur_d)
    answer += get_point(cur[0], cur[1])
print(answer)
