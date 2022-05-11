# 문제
# 상근이는 빈 공간과 벽으로 이루어진 건물에 갇혀있다. 건물의 일부에는 불이 났고, 상근이는 출구를 향해 뛰고 있다.
#
# 매 초마다, 불은 동서남북 방향으로 인접한 빈 공간으로 퍼져나간다. 벽에는 불이 붙지 않는다. 상근이는 동서남북 인접한 칸으로 이동할 수 있으며, 1초가 걸린다. 상근이는 벽을 통과할 수 없고, 불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 이동할 수 없다. 상근이가 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동할 수 있다.
#
# 빌딩의 지도가 주어졌을 때, 얼마나 빨리 빌딩을 탈출할 수 있는지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스는 최대 100개이다.
#
# 각 테스트 케이스의 첫째 줄에는 빌딩 지도의 너비와 높이 w와 h가 주어진다. (1 ≤ w,h ≤ 1000)
#
# 다음 h개 줄에는 w개의 문자, 빌딩의 지도가 주어진다.
#
# '.': 빈 공간
# '#': 벽
# '@': 상근이의 시작 위치
# '*': 불
# 각 지도에 @의 개수는 하나이다.
#
# 출력
# 각 테스트 케이스마다 빌딩을 탈출하는데 가장 빠른 시간을 출력한다. 빌딩을 탈출할 수 없는 경우에는 "IMPOSSIBLE"을 출력한다.
import collections
t=int(input())
dy, dx=[0, 1, 0, -1], [1, 0, -1, 0]
def fire_move():
    global fire
    new_fire=[]
    f=collections.deque(fire)
    while f:
        y, x=f.popleft()
        for i in range(4):
            ny, nx=y+dy[i], x+dx[i]
            if 0<=ny<h and 0<=nx<w and grid[ny][nx]!='#' and grid[ny][nx]!='*':
                new_fire.append((ny, nx))
                grid[ny][nx]='*'
    fire=new_fire[:]
def sg_move(y, x):
    q=collections.deque()
    q.append((y, x, 0))
    visited=[[False for _ in range(w)] for _ in range(h)]
    time=0
    while q:
        y, x, cnt=q.popleft()
        if cnt>=time:
            fire_move()
            time+=1
        for i in range(4):
            ny, nx=y+dy[i], x+dx[i]
            if 0<=ny<h and 0<=nx<w and not visited[ny][nx] and grid[ny][nx]=='.':
                visited[ny][nx]=True
                q.append((ny, nx, cnt+1))
            elif not (0<=ny<h and 0<=nx<w):
                return cnt+1
    return 0
for _ in range(t):
    w, h=map(int, input().split())
    grid=[list(str(input())) for _ in range(h)]
    sg=[]
    fire=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]=='@':
                sg=[i, j]
            if grid[i][j]=='*':
                fire.append((i, j))
    answer=sg_move(sg[0], sg[1])
    if not answer:
        answer='IMPOSSIBLE'
    print(answer)
