# 문제
# 러시아 가스를 크로아티아로 운반하기 위해 자그레브와 모스코바는 파이프라인을 디자인하고 있다. 두 사람은 실제 디자인을 하기 전에 파이프 매니아 게임을 이용해서 설계를 해보려고 한다.
#
# 이 게임에서 유럽은 R행 C열로 나누어져 있다. 각 칸은 비어있거나, 아래 그림과 같은 일곱가지 기본 블록으로 이루어져 있다.
#
# 블록 '|'	블록 '-'	블록 '+'	블록 '1'	블록 '2'	블록 '3'	블록 '4'
#
# 가스는 모스크바에서 자그레브로 흐른다. 가스는 블록을 통해 양방향으로 흐를 수 있다. '+'는 특별한 블록으로, 아래 예시처럼 두 방향 (수직, 수평)으로 흘러야 한다.
#
#
#
# 파이프 라인의 설계를 마친 후 두 사람은 잠시 저녁을 먹으러 갔다. 그 사이 해커가 침임해 블록 하나를 지웠다. 지운 블록은 빈 칸이 되어있다.
#
# 해커가 어떤 칸을 지웠고, 그 칸에는 원래 어떤 블록이 있었는지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 유럽의 크기 R과 C가 주어진다. (1 ≤ R, C ≤ 25)
#
# 다음 R개 줄에는 C개 글자가 주어지며, 다음과 같은 글자로 이루어져 있다.
#
# 빈칸을 나타내는 '.'
# 블록을 나타내는 '|'(아스키 124), '-','+','1','2','3','4'
# 모스크바의 위치를 나타내는 'M'과 자그레브를 나타내는 'Z'. 두 글자는 한 번만 주어진다.
# 항상 답이 존재하고, 가스의 흐름이 유일한 경우만 입력으로 주어진다, 또, 모스크바와 자그레브가 하나의 블록과 인접해 있는 입력만 주어진다. 또, 불필요한 블록이 존재하지 않는다. 즉, 없어진 블록을 추가하면, 모든 블록에 가스가 흐르게 된다.
#
# 출력
# 지워진 블록의 행과 열 위치를 출력하고, 어떤 블록이었는지를 출력한다.
from collections import deque
r, c = map(int, input().split())
grid = [list(str(input())) for _ in range(r)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
mapping = {'1': {2: 1, 3: 0}, '2': {1: 0, 2: 3}, '3': {0: 3, 1: 2}, '4': {0: 1, 3: 2}}
dot = {0: 2, 1: 3, 2: 0, 3: 1}
sy, sx = 0, 0
for i in range(r):
    for j in range(c):
        if grid[i][j] == 'M':
            sy, sx = i, j
def chk(ny, nx, cur_d):
    if cur_d == 0 and grid[ny][nx] in ('3', '4'):
        return True
    if cur_d == 1 and grid[ny][nx] in ('2', '3'):
        return True
    if cur_d == 2 and grid[ny][nx] in ('1', '2'):
        return True
    if cur_d == 3 and grid[ny][nx] in ('1', '4'):
        return True
    return False
def m_to_z():
    q = deque()
    q.append((sy, sx, -1))
    visited = [[False for _ in range(c)] for _ in range(r)]
    visited[sy][sx] = True
    while q:
        y, x, d = q.popleft()
        if grid[y][x] == 'M':
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < r and 0 <= nx < c and grid[ny][nx] != '.':
                    visited[ny][nx] = True
                    q.append((ny, nx, i))
        elif grid[y][x] == '|' or grid[y][x] == '-':
            ny, nx = y+dy[d], x+dx[d]
            if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx, d))
        elif grid[y][x] == '+':
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx, i))
        elif grid[y][x] in ('1', '2', '3', '4'):
            nxt_d = mapping[grid[y][x]][d]
            ny, nx = y+dy[nxt_d], x+dx[nxt_d]
            if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx, nxt_d))
        elif grid[y][x] == '.':
            tmp = []
            for i in range(4):
                if i == dot[d]:
                    continue
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < r and 0 <= nx < c:
                    if grid[ny][nx] != '.':
                        if grid[ny][nx] == '+' or (i in (1, 3) and grid[ny][nx] == '|') or (i in (0, 2) and grid[ny][nx] == '-') or chk(ny, nx, i):
                            tmp.append(i)
            if len(tmp) == 1:
                if d == tmp[0]:
                    if tmp[0] == 1 or tmp[0] == 3:
                        result = [y+1, x+1, '|']
                        return result
                    if tmp[0] == 0 or tmp[0] == 2:
                        result = [y+1, x+1, '-']
                        return result
                else:
                    for key, value in mapping.items():
                        for before, nxt in mapping[key].items():
                            if d == before and tmp[0] == nxt:
                                result = [y+1, x+1, key]
                                return result
            elif len(tmp) == 3:
                result = [y+1, x+1, '+']
                return result
print(*m_to_z())
