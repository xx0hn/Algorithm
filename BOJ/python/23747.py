# 문제
# 한별이는 출근하던 도중 이세계 대환장 버스에 치였다.
#
#
#
# 그림 B.1: 이세계 대환장 버스
#
#
#
# 그림 B.2: 출근하는 한별이
#
# 올해 휴가를 전부 써 버려 당장 판교로 돌아가야 하는 한별이는 돌아가기 위한 방법을 어떻게든 찾아보기 위해 이세계를 돌아다녀 보려고 한다.
#
# 이세계는 $R\times C$의 격자로 되어 있다. 지금은 밤이어서 한별이는 자신이 위치한 칸 및 그 칸에서 위, 아래, 왼쪽 또는 오른쪽으로 인접한 칸만을 볼 수 있지만, 와드를 설치하면 조금 더 넓은 영역의 시야를 확보할 수 있다. 구체적으로는, 격자의 모든 칸은 각각 어떤 영역 하나에 속해 있는데, 와드를 놓으면 와드가 놓인 칸이 속한 영역에 있는 모든 칸을 볼 수 있게 된다.
#
# 한별이의 여행 기록이 주어질 때 한별이가 얼마나 넓은 시야를 확보했을지 계산해 보자.
#
# 입력
# 첫 번째 줄에는 격자의 크기를 나타내는 두 정수 $R$과 $C$가 주어진다. ($1 \le R,C \le 1\,000$)
#
# 다음 줄부터 $R$개의 줄에 걸쳐 격자의 정보가 주어진다. 각 줄은 $C$개의 알파벳 소문자로 이루어져 있으며, 위, 아래, 왼쪽 또는 오른쪽으로 인접해 있는 칸이 같은 문자라는 것은 두 칸이 같은 영역에 속해 있음을 의미한다.
#
# 다음 줄에는 한별이가 이세계에 떨어진 위치를 나타내는 두 정수 $H_R$, $H_C$가 주어진다. 이는 한별이가 위에서 $H_R$번째 줄, 왼쪽에서 $H_C$번째 칸에 떨어졌음을 의미한다. ($1 \le H_R \le R$, $1 \le H_C \le C$)
#
# 마지막 줄에는 한별이의 여행 기록을 나타내는 $200\,000$글자 이하의 문자열이 주어진다. 여행 기록의 각 문자는 U, D, L, R, W 중 하나로 이루어져 있으며, U, D, L, R은 각각 위, 아래, 왼쪽, 오른쪽으로 한 칸 이동했다는 뜻이고, W는 지금 있는 칸에 와드를 설치했다는 뜻이다. 한별이가 격자를 벗어나는 경우는 주어지지 않는다.
#
# 출력
#  $R$개의 줄에 걸쳐 한별이의 시야를 출력한다. 각 줄은 $C$개의 문자로 되어 있어야 하며, $R$번째 줄 $C$번째 문자가 .이라면 한별이의 시야에 해당 칸이 들어와 있다는 뜻이고 #이라면 그렇지 않다는 뜻이다.
from collections import deque
r, c = map(int, input().split())
grid = [list(str(input())) for _ in range(r)]
hy, hx = map(int, input().split())
hy, hx = hy-1, hx-1
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
mapping = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
commands = list(str(input()))
answer = [['#' for _ in range(c)] for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]
num = 1
def wd(y, x, num):
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    tmp = grid[y][x]
    grid[y][x] = num
    answer[y][x] = '.'
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < r and 0 <= nx < c and grid[ny][nx] == tmp and not visited[ny][nx]:
                grid[ny][nx] = num
                answer[ny][nx] = '.'
                visited[ny][nx] = True
                q.append((ny, nx))
for command in commands:
    if command == 'W':
        if str(grid[hy][hx]).isalpha():
            wd(hy, hx, num)
            num += 1
    else:
        d = mapping[command]
        hy, hx = hy+dy[d], hx+dx[d]
answer[hy][hx] = '.'
for i in range(4):
    ny, nx = hy+dy[i], hx+dx[i]
    if 0 <= ny < r and 0 <= nx < c:
        answer[ny][nx] = '.'
for i in range(r):
    print(''.join(answer[i]))
