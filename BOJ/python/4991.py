# 문제
# 오늘은 직사각형 모양의 방을 로봇 청소기를 이용해 청소하려고 한다. 이 로봇 청소기는 유저가 직접 경로를 설정할 수 있다.
#
# 방은 크기가 1×1인 정사각형 칸으로 나누어져 있으며, 로봇 청소기의 크기도 1×1이다. 칸은 깨끗한 칸과 더러운 칸으로 나누어져 있으며, 로봇 청소기는 더러운 칸을 방문해서 깨끗한 칸으로 바꿀 수 있다.
#
# 일부 칸에는 가구가 놓여져 있고, 가구의 크기도 1×1이다. 로봇 청소기는 가구가 놓여진 칸으로 이동할 수 없다.
#
# 로봇은 한 번 움직일 때, 인접한 칸으로 이동할 수 있다. 또, 로봇은 같은 칸을 여러 번 방문할 수 있다.
#
# 방의 정보가 주어졌을 때, 더러운 칸을 모두 깨끗한 칸으로 만드는데 필요한 이동 횟수의 최솟값을 구하는 프로그램을 작성하시오.
#
# 입력
# 입력은 여러 개의 테스트케이스로 이루어져 있다.
#
# 각 테스트 케이스의 첫째 줄에는 방의 가로 크기 w와 세로 크기 h가 주어진다. (1 ≤ w, h ≤ 20) 둘째 줄부터 h개의 줄에는 방의 정보가 주어진다. 방의 정보는 4가지 문자로만 이루어져 있으며, 각 문자의 의미는 다음과 같다.
#
# .: 깨끗한 칸
# *: 더러운 칸
# x: 가구
# o: 로봇 청소기의 시작 위치
# 더러운 칸의 개수는 10개를 넘지 않으며, 로봇 청소기의 개수는 항상 하나이다.
#
# 입력의 마지막 줄에는 0이 두 개 주어진다.
#
# 출력
# 각각의 테스트 케이스마다 더러운 칸을 모두 깨끗한 칸으로 바꾸는 이동 횟수의 최솟값을 한 줄에 하나씩 출력한다. 만약, 방문할 수 없는 더러운 칸이 존재하는 경우에는 -1을 출력한다.
from collections import deque
from itertools import permutations
def cleaning(y, x):
    q = deque()
    q.append((y, x))
    visited = [[0 for _ in range(w)] for _ in range(h)]
    visited[y][x] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] != 'x' and not visited[ny][nx]:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))
    return visited
while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break
    grid = [list(str(input())) for _ in range(h)]
    dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
    dust = []
    robot = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '*':
                dust.append((i, j))
            if grid[i][j] == 'o':
                robot = [i, j]
    r_d, chk = [], True
    c = cleaning(robot[0], robot[1])
    for y, x in dust:
        if not c[y][x]:
            chk = False
            break
        r_d.append(c[y][x]-1)
    if not chk:
        print(-1)
        continue
    d_d = [[0 for _ in range(len(dust))] for _ in range(len(dust))]
    for i in range(len(dust)-1):
        c = cleaning(dust[i][0], dust[i][1])
        for j in range(i+1, len(dust)):
            d_d[i][j] = c[dust[j][0]][dust[j][1]]-1
            d_d[j][i] = d_d[i][j]
    points = list(permutations([i for i in range(len(d_d))]))
    answer = 1e9
    for i in points:
        dist = 0
        dist += r_d[i[0]]
        start = i[0]
        for j in range(1, len(i)):
            end = i[j]
            dist += d_d[start][end]
            start = end
        answer = min(answer, dist)
    print(answer)
