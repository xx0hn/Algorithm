# 문제
# 두 마리의 백조가 호수에서 살고 있었다. 그렇지만 두 마리는 호수를 덮고 있는 빙판으로 만나지 못한다.
#
# 호수는 행이 R개, 열이 C개인 직사각형 모양이다. 어떤 칸은 얼음으로 덮여있다.
#
# 호수는 차례로 녹는데, 매일 물 공간과 접촉한 모든 빙판 공간은 녹는다. 두 개의 공간이 접촉하려면 가로나 세로로 닿아 있는 것만 (대각선은 고려하지 않는다) 생각한다.
#
# 아래에는 세 가지 예가 있다.
#
# ...XXXXXX..XX.XXX ....XXXX.......XX .....XX..........
# ....XXXXXXXXX.XXX .....XXXX..X..... ......X..........
# ...XXXXXXXXXXXX.. ....XXX..XXXX.... .....X.....X.....
# ..XXXXX..XXXXXX.. ...XXX....XXXX... ....X......XX....
# .XXXXXX..XXXXXX.. ..XXXX....XXXX... ...XX......XX....
# XXXXXXX...XXXX... ..XXXX.....XX.... ....X............
# ..XXXXX...XXX.... ....XX.....X..... .................
# ....XXXXX.XXX.... .....XX....X..... .................
#       처음               첫째 날             둘째 날
# 백조는 오직 물 공간에서 세로나 가로로만(대각선은 제외한다) 움직일 수 있다.
#
# 며칠이 지나야 백조들이 만날 수 있는 지 계산하는 프로그램을 작성하시오.
#
# 입력
# 입력의 첫째 줄에는 R과 C가 주어진다. 단, 1 ≤ R, C ≤ 1500.
#
# 다음 R개의 줄에는 각각 길이 C의 문자열이 하나씩 주어진다. '.'은 물 공간, 'X'는 빙판 공간, 'L'은 백조가 있는 공간으로 나타낸다.
#
# 출력
# 첫째 줄에 문제에서 주어진 걸리는 날을 출력한다.
from collections import deque
r, c = map(int, input().split())
grid, swan = [], []
water = deque()
for i in range(r):
    tmp = list(str(input()))
    for j in range(c):
        if tmp[j] == '.' or tmp[j] == 'L':
            water.append((i, j))
        if tmp[j] == 'L':
            swan.append((i, j))
    grid.append(tmp)
day = -1
q = deque()
q.append((swan[0][0], swan[0][1]))
visited = [[False for _ in range(c)] for _ in range(r)]
visited[swan[0][0]][swan[0][1]] = True
dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]

def meet_swan():
    nxt_q = deque()
    while q:
        y, x = q.popleft()
        if (y, x) == (swan[1][0], swan[1][1]):
            return True, None
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx]:
                if grid[ny][nx] == '.' or grid[ny][nx] == 'L':
                    q.append((ny, nx))
                if grid[ny][nx] == 'X':
                    nxt_q.append((ny, nx))
                visited[ny][nx] = True
    return False, nxt_q

def melt_ice():
    nxt_water = deque()
    while water:
        y, x = water.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < r and 0 <= nx < c and grid[ny][nx] == 'X':
                nxt_water.append((ny, nx))
                grid[ny][nx] = '.'
    return nxt_water

while True:
    day += 1
    chk, nxt_q = meet_swan()
    if chk:
        break
    water = melt_ice()
    q = nxt_q
print(day)
