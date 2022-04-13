# 문제
# N×M 크기의 보드와 4개의 버튼으로 이루어진 게임이 있다. 보드는 1×1크기의 정사각형 칸으로 나누어져 있고, 각각의 칸은 비어있거나, 벽이다. 두 개의 빈 칸에는 동전이 하나씩 놓여져 있고, 두 동전의 위치는 다르다.
#
# 버튼은 "왼쪽", "오른쪽", "위", "아래"와 같이 4가지가 있다. 버튼을 누르면 두 동전이 버튼에 쓰여 있는 방향으로 동시에 이동하게 된다.
#
# 동전이 이동하려는 칸이 벽이면, 동전은 이동하지 않는다.
# 동전이 이동하려는 방향에 칸이 없으면 동전은 보드 바깥으로 떨어진다.
# 그 외의 경우에는 이동하려는 방향으로 한 칸 이동한다.이동하려는 칸에 동전이 있는 경우에도 한 칸 이동한다.
# 두 동전 중 하나만 보드에서 떨어뜨리기 위해 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 보드의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 20)
#
# 둘째 줄부터 N개의 줄에는 보드의 상태가 주어진다.
#
# o: 동전
# .: 빈 칸
# #: 벽
# 동전의 개수는 항상 2개이다.
#
# 출력
# 첫째 줄에 두 동전 중 하나만 보드에서 떨어뜨리기 위해 눌러야 하는 버튼의 최소 횟수를 출력한다. 만약, 두 동전을 떨어뜨릴 수 없거나, 버튼을 10번보다 많이 눌러야 한다면, -1을 출력한다.
import collections
n, m=map(int, input().split())
board=[list(str(input())) for _ in range(n)]
q=collections.deque()
tmp=[]
for i in range(n):
    for j in range(m):
        if board[i][j]=='o':
            tmp.append(i)
            tmp.append(j)
q.append((tmp[0], tmp[1], tmp[2], tmp[3], 0))
dy, dx=[0, 0, -1, 1], [-1, 1, 0, 0]
def bfs():
    while q:
        y1, x1, y2, x2, cnt=q.popleft()
        if cnt>=10:
            break
        for i in range(4):
            ny1, nx1, ny2, nx2=y1+dy[i], x1+dx[i], y2+dy[i], x2+dx[i]
            if not (0<=ny1<n and 0<=nx1<m) and not (0<=ny2<n and 0<=nx2<m):
                continue
            if not (0<=ny1<n and 0<=nx1<m):
                return cnt+1
            if not (0<=ny2<n and 0<=nx2<m):
                return cnt+1
            if board[ny1][nx1]=='#':
                ny1, nx1=y1, x1
            if board[ny2][nx2]=='#':
                ny2, nx2=y2, x2
            q.append((ny1, nx1, ny2, nx2, cnt+1))
    return -1
answer=bfs()
print(answer)
