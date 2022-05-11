# 문제
# 크기가 1×1인 정사각형으로 나누어진 W×H 크기의 지도가 있다. 지도의 각 칸은 빈 칸이거나 벽이며, 두 칸은 'C'로 표시되어 있는 칸이다.
#
# 'C'로 표시되어 있는 두 칸을 레이저로 통신하기 위해서 설치해야 하는 거울 개수의 최솟값을 구하는 프로그램을 작성하시오. 레이저로 통신한다는 것은 두 칸을 레이저로 연결할 수 있음을 의미한다.
#
# 레이저는 C에서만 발사할 수 있고, 빈 칸에 거울('/', '\')을 설치해서 방향을 90도 회전시킬 수 있다.
#
# 아래 그림은 H = 8, W = 7인 경우이고, 빈 칸은 '.', 벽은 '*'로 나타냈다. 왼쪽은 초기 상태, 오른쪽은 최소 개수의 거울을 사용해서 두 'C'를 연결한 것이다.
#
# 7 . . . . . . .         7 . . . . . . .
# 6 . . . . . . C         6 . . . . . /-C
# 5 . . . . . . *         5 . . . . . | *
# 4 * * * * * . *         4 * * * * * | *
# 3 . . . . * . .         3 . . . . * | .
# 2 . . . . * . .         2 . . . . * | .
# 1 . C . . * . .         1 . C . . * | .
# 0 . . . . . . .         0 . \-------/ .
#   0 1 2 3 4 5 6           0 1 2 3 4 5 6
# 입력
# 첫째 줄에 W와 H가 주어진다. (1 ≤ W, H ≤ 100)
#
# 둘째 줄부터 H개의 줄에 지도가 주어진다. 지도의 각 문자가 의미하는 것은 다음과 같다.
#
# .: 빈 칸
# *: 벽
# C: 레이저로 연결해야 하는 칸
# 'C'는 항상 두 개이고, 레이저로 연결할 수 있는 입력만 주어진다.
#
# 출력
# 첫째 줄에 C를 연결하기 위해 설치해야 하는 거울 개수의 최솟값을 출력한다.
import collections
w, h=map(int, input().split())
board=[str(input()) for _ in range(h)]
c=[]
for i in range(h):
    for j in range(w):
        if board[i][j]=='C':
            c.append((i, j))
dy, dx=[-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(y, x):
    q=collections.deque()
    q.append((y, x))
    visited=[[1e9 for _ in range(w)] for _ in range(h)]
    visited[y][x]=0
    while q:
        y, x=q.popleft()
        for i in range(4):
            ny, nx=y+dy[i], x+dx[i]
            while True:
                if not (0<=ny<h and 0<=nx<w):
                    break
                if board[ny][nx]=='*':
                    break
                if visited[ny][nx]<visited[y][x]+1:
                    break
                q.append((ny, nx))
                visited[ny][nx]=visited[y][x]+1
                ny, nx=ny+dy[i], nx+dx[i]
    return visited
answer=bfs(c[0][0], c[0][1])
print(answer[c[1][0]][c[1][1]]-1)
