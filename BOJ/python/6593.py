# 문제
# 당신은 상범 빌딩에 갇히고 말았다. 여기서 탈출하는 가장 빠른 길은 무엇일까? 상범 빌딩은 각 변의 길이가 1인 정육면체(단위 정육면체)로 이루어져있다. 각 정육면체는 금으로 이루어져 있어 지나갈 수 없거나, 비어있어서 지나갈 수 있게 되어있다. 당신은 각 칸에서 인접한 6개의 칸(동,서,남,북,상,하)으로 1분의 시간을 들여 이동할 수 있다. 즉, 대각선으로 이동하는 것은 불가능하다. 그리고 상범 빌딩의 바깥면도 모두 금으로 막혀있어 출구를 통해서만 탈출할 수 있다.
#
# 당신은 상범 빌딩을 탈출할 수 있을까? 만약 그렇다면 얼마나 걸릴까?
#
# 입력
# 입력은 여러 개의 테스트 케이스로 이루어지며, 각 테스트 케이스는 세 개의 정수 L, R, C로 시작한다. L(1 ≤ L ≤ 30)은 상범 빌딩의 층 수이다. R(1 ≤ R ≤ 30)과 C(1 ≤ C ≤ 30)는 상범 빌딩의 한 층의 행과 열의 개수를 나타낸다.
#
# 그 다음 각 줄이 C개의 문자로 이루어진 R개의 행이 L번 주어진다. 각 문자는 상범 빌딩의 한 칸을 나타낸다. 금으로 막혀있어 지나갈 수 없는 칸은 '#'으로 표현되고, 비어있는 칸은 '.'으로 표현된다. 당신의 시작 지점은 'S'로 표현되고, 탈출할 수 있는 출구는 'E'로 표현된다. 각 층 사이에는 빈 줄이 있으며, 입력의 끝은 L, R, C가 모두 0으로 표현된다. 시작 지점과 출구는 항상 하나만 있다.
#
# 출력
# 각 빌딩에 대해 한 줄씩 답을 출력한다. 만약 당신이 탈출할 수 있다면 다음과 같이 출력한다.
#
# Escaped in x minute(s).
# 여기서 x는 상범 빌딩을 탈출하는 데에 필요한 최단 시간이다.
#
# 만일 탈출이 불가능하다면, 다음과 같이 출력한다.
#
# Trapped!
from collections import deque
def bfs(sz, sy, sx):
    q = deque()
    q.append((sz, sy, sx, 0))
    visited = [[[False for _ in range(c)] for _ in range(r)] for _ in range(l)]
    visited[sz][sy][sx] = True
    while q:
        z, y, x, time = q.popleft()
        if (z, y, x) == (ez, ey, ex):
            return time
        for i in range(6):
            nz, ny, nx = z+dz[i], y+dy[i], x+dx[i]
            if 0 <= nz < l and 0 <= ny < r and 0 <= nx < c and grid[nz][ny][nx] != '#' and not visited[nz][ny][nx]:
                visited[nz][ny][nx] = True
                q.append((nz, ny, nx, time+1))
    return -1
while True:
    l, r, c = map(int, input().split())
    if (l, r, c) == (0, 0, 0):
        break
    grid = []
    for _ in range(l):
        tmp = [list(str(input())) for _ in range(r)]
        grid.append(tmp)
        tmp1 = input()
    sz, sy, sx = 0, 0, 0
    ez, ey, ex = 0, 0, 0
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if grid[i][j][k] == 'S':
                    sz, sy, sx = i, j, k
                if grid[i][j][k] == 'E':
                    ez, ey, ex = i, j, k
    dz, dy, dx = [0, 0, 0, 0, 1, -1], [1, 0, -1, 0, 0, 0], [0, 1, 0, -1, 0, 0]
    answer = bfs(sz, sy, sx)
    if answer > 0:
        print("Escaped in "+str(answer)+" minute(s).")
    else:
        print("Trapped!")
