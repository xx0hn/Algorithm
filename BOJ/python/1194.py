# 문제
# 지금 민식이가 계획한 여행은 달이 맨 처음 뜨기 시작할 때 부터, 준비했던 여행길이다. 하지만, 매번 달이 차오를 때마다 민식이는 어쩔 수 없는 현실의 벽 앞에서 다짐을 포기하고 말았다.
#
# 민식이는 매번 자신의 다짐을 말하려고 노력했지만, 말을 하면 아무도 못 알아들을 것만 같아서, 지레 겁먹고 벙어리가 되어버렸다. 결국 민식이는 모두 잠든 새벽 네시 반쯤 홀로 일어나, 창 밖에 떠있는 달을 보았다.
#
# 하루밖에 남지 않았다. 달은 내일이면 다 차오른다. 이번이 마지막기회다. 이걸 놓치면 영영 못간다.
#
# 영식이는 민식이가 오늘도 여태것처럼 그냥 잠 들어버려서 못 갈지도 모른다고 생각했다. 하지만 그러기엔 민식이의 눈에는 저기 뜬 달이 너무나 떨렸다.
#
# 민식이는 지금 미로 속에 있다. 미로는 직사각형 모양이고, 여행길을 떠나기 위해 미로를 탈출하려고 한다. 미로는 다음과 같이 구성되어져있다.
#
# 빈 칸: 언제나 이동할 수 있다. ('.')
# 벽: 절대 이동할 수 없다. ('#')
# 열쇠: 언제나 이동할 수 있다. 이 곳에 처음 들어가면 열쇠를 집는다. ('a', 'b', 'c', 'd', 'e', 'f')
# 문: 대응하는 열쇠가 있을 때만 이동할 수 있다. ('A', 'B', 'C', 'D', 'E', 'F')
# 민식이의 현재 위치: 빈 곳이고, 민식이가 현재 서 있는 곳이다. ('0')
# 출구: 달이 차오르기 때문에, 민식이가 가야하는 곳이다. 이 곳에 오면 미로를 탈출한다. ('1')
# 달이 차오르는 기회를 놓치지 않기 위해서, 미로를 탈출하려고 한다. 한 번의 움직임은 현재 위치에서 수평이나 수직으로 한 칸 이동하는 것이다.
#
# 민식이가 미로를 탈출하는데 걸리는 이동 횟수의 최솟값을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 미로의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 50) 둘째 줄부터 N개의 줄에 미로의 모양이 주어진다. 같은 타입의 열쇠가 여러 개 있을 수 있고, 문도 마찬가지이다. 그리고, 문에 대응하는 열쇠가 없을 수도 있다. '0'은 한 개, '1'은 적어도 한 개 있다. 열쇠는 여러 번 사용할 수 있다.
#
# 출력
# 첫째 줄에 민식이가 미로를 탈출하는데 드는 이동 횟수의 최솟값을 출력한다. 만약 민식이가 미로를 탈출 할 수 없으면, -1을 출력한다.
from collections import deque
n, m = map(int, input().split())
grid = [list(str(input())) for _ in range(n)]
sy, sx = 0, 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '0':
            sy, sx = i, j
            grid[i][j] = '.'
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
visited = [[[0 for _ in range(64)] for _ in range(m)] for _ in range(n)]
mapping = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
def bfs():
    q = deque()
    q.append((sy, sx, 0))
    visited[sy][sx][0] = 1
    while q:
        y, x, key = q.popleft()
        if grid[y][x] == '1':
            return visited[y][x][key]-1
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] != '#' and not visited[ny][nx][key]:
                if str(grid[ny][nx]).isalpha():
                    if ord(str(grid[ny][nx])) < ord('a'):
                        if key & (1<<(ord(str(grid[ny][nx]))-ord('A'))):
                            visited[ny][nx][key] = visited[y][x][key]+1
                            q.append((ny, nx, key))
                    else:
                        new_key = key | (1<<ord(str(grid[ny][nx]))-ord('a'))
                        if not visited[ny][nx][new_key]:
                            visited[ny][nx][new_key] = visited[y][x][key]+1
                            q.append((ny, nx, new_key))
                else:
                    visited[ny][nx][key] = visited[y][x][key]+1
                    q.append((ny, nx, key))
    return -1
print(bfs())
