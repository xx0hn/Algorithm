# 문제
#
#
# 탐험가 테라는 얼음 미로에 갇혔다. 얼음 미로의 바닥은 빙판으로 되어 있어 발을 내디디면 바위에 부딪힐 때까지 미끄러진다. 예를 들어, 위 그림에서 테라가 왼쪽 방향으로 이동한다면 중간에 멈출 수 없고 왼쪽 바위에 부딪힐 때까지 미끄러진다. 얼음 미로 바깥은 절벽이기 때문에 빠지면 탈출할 수 없다.
#
# 얼음 미로에는 $4$가지 오브젝트가 있다.
#
#   테라 : 얼음 미로에 갇힌 탐험가. 상하좌우 $4$방향으로 이동할 수 있다. 얼음 미로에 단 $1$명의 테라만 존재한다. 테라가 최초 위치한 빙판의 미끌 시간은 $0$이다.
#   바위 : 통과할 수 없다. 미끄러지다 부딪히면 앞에서 멈춘다.
#   구멍 : 이곳에 빠지면 영영 탈출할 수 없다.
#   출구 : 이곳에 방문하는 즉시 얼음 미로를 탈출한다. 얼음 미로에 단 $1$개의 출구만 존재한다.
# 어떤 빙판 위에서 미끄러지는 데 걸리는 시간을 미끌 시간이라고 하자. 각 빙판마다 미끌 시간은 다를 수 있다.
#
# 테라가 어느 한쪽 방향으로 이동할 때, 테라가 미끄러지는 동안 위치한 빙판의 미끌 시간을 더하면 이동 시간을 구할 수 있다. 단, 이동 시간 계산과 관련하여 두 가지 규칙이 있다.
#
#
#
# 테라가 어느 한쪽 방향으로 이동을 시작할 때, 시작 빙판의 미끌 시간은 포함하지 않는다.
# 테라가 출구로 들어갈 때, 출구 빙판의 미끌 시간은 포함하지 않는다.
# 위 그림에서 테라가 위로 이동할 때의 이동 시간을 계산하자. 테라가 현재 서 있는, 시작 빙판의 미끌 시간 $4$와 출구 빙판의 미끌 시간 $0$을 제외하면 $1 + 2 = 3$ 만큼의 시간이 걸린 뒤 출구를 통해 탈출함을 알 수 있다.
#
# 저체온증이 시작된 테라는 얼음 미로를 가능한 한 빨리 탈출하고 싶다. 얼음 미로를 탈출하는 데 걸리는 최단 시간을 계산하자.
#
# 입력
# 첫 번째 줄에는 얼음 미로의 가로 크기를 나타내는 정수 $W$($2 \le W \le 500$), 세로 크기를 나타내는 정수 $H$($2 \le H \le 500$)가 주어진다.
#
# 두 번째 줄부터 $H$개의 줄에 걸쳐 얼음 미로에 대한 정보가 주어진다.
#
# 테라는 T, 바위는 R, 구멍은 H, 출구는 E로 나타낸다.
#
# 빙판의 미끌 시간 $t$는 $0$ 이상 $9$ 이하의 정수로 나타낸다.
#
# 출력
# 얼음 미로를 탈출할 수 있다면 최단 탈출 시간을 출력한다.
#
# 얼음 미로를 탈출할 수 없다면 -1을 출력한다.
import heapq
w, h = map(int, input().split())
grid = [list(str(input())) for _ in range(h)]
tera = []
exit = ()
for i in range(h):
    for j in range(w):
        if grid[i][j] == 'T':
            tera = [i, j]
            grid[i][j] = 0
        if grid[i][j] == 'E':
            exit = (i, j)
            grid[i][j] = 0
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
def move(y, x, d):
    time = 0
    path = []
    while True:
        path.append(int(grid[y][x]))
        y, x = y+dy[d], x+dx[d]
        if not (0 <= y < h) or not (0 <= x < w) or grid[y][x] == 'H':
            return y, x, 1e9
        if grid[y][x] == 'R':
            y, x = y-dy[d], x-dx[d]
            break
        if (y, x) == exit:
            break
    time += (sum(path[1:]))
    return y, x, time
def dijkstra():
    q = []
    heapq.heappush(q, (0, tera[0], tera[1]))
    dist = [[1e9 for _ in range(w)] for _ in range(h)]
    dist[tera[0]][tera[1]] = 0
    while q:
        time, y, x = heapq.heappop(q)
        if time > dist[y][x]:
            continue
        for i in range(4):
            nxt_y, nxt_x, nxt_time = move(y, x, i)
            nxt_time += time
            if 0 <= nxt_y < h and 0 <= nxt_x < w and dist[nxt_y][nxt_x] > nxt_time:
                dist[nxt_y][nxt_x] = nxt_time
                heapq.heappush(q, (nxt_time, nxt_y, nxt_x))
    return dist[exit[0]][exit[1]]
answer = dijkstra()
if answer == 1e9:
    answer = -1
print(answer)
