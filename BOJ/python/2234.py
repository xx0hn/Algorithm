# 문제
#
#
# 대략 위의 그림과 같이 생긴 성곽이 있다. 굵은 선은 벽을 나타내고, 점선은 벽이 없어서 지나다닐 수 있는 통로를 나타낸다. 이러한 형태의 성의 지도를 입력받아서 다음을 계산하는 프로그램을 작성하시오.
#
# 이 성에 있는 방의 개수
# 가장 넓은 방의 넓이
# 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
# 위의 예에서는 방은 5개고, 가장 큰 방은 9개의 칸으로 이루어져 있으며, 위의 그림에서 화살표가 가리키는 벽을 제거하면 16인 크기의 방을 얻을 수 있다.
#
# 성은 M × N(1 ≤ M, N ≤ 50)개의 정사각형 칸으로 이루어진다. 성에는 최소 두 개의 방이 있어서, 항상 하나의 벽을 제거하여 두 방을 합치는 경우가 있다.
#
# 입력
# 첫째 줄에 두 정수 N, M이 주어진다. 다음 M개의 줄에는 N개의 정수로 벽에 대한 정보가 주어진다. 벽에 대한 정보는 한 정수로 주어지는데, 서쪽에 벽이 있을 때는 1을, 북쪽에 벽이 있을 때는 2를, 동쪽에 벽이 있을 때는 4를, 남쪽에 벽이 있을 때는 8을 더한 값이 주어진다. 참고로 이진수의 각 비트를 생각하면 쉽다. 따라서 이 값은 0부터 15까지의 범위 안에 있다.
#
# 출력
# 첫째 줄에 1의 답을, 둘째 줄에 2의 답을, 셋째 줄에 3의 답을 출력한다.
from collections import deque
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
cnt = [[0 for _ in range(n)] for _ in range(m)]
rooms = [[0 for _ in range(n)] for _ in range(m)]
dy, dx = [0, -1, 0, 1], [-1, 0, 1, 0]
room_cnt = 0
largest_room = 0
answer = 0
def get_room(sy, sx):
    q = deque()
    q.append((sy, sx))
    path = [(sy, sx)]
    rooms[sy][sx] = room_cnt
    result = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < m and 0 <= nx < n and not rooms[ny][nx]:
                if not grid[y][x] & (1<<i):
                    q.append((ny, nx))
                    path.append((ny, nx))
                    rooms[ny][nx] = room_cnt
                    result += 1
    for y, x in path:
        cnt[y][x] = result
for i in range(m):
    for j in range(n):
        if not rooms[i][j]:
            room_cnt += 1
            get_room(i, j)
for i in range(m):
    for j in range(n):
        for d in range(4):
            ni, nj = i+dy[d], j+dx[d]
            if 0 <= ni < m and 0 <= nj < n:
                if rooms[i][j] != rooms[ni][nj]:
                    answer = max(answer, cnt[i][j]+cnt[ni][nj])
        if largest_room < cnt[i][j]:
            largest_room = cnt[i][j]
print(room_cnt)
print(largest_room)
print(answer)
