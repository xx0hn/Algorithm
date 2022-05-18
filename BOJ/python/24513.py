# 문제
# 여기 $N$ x $M$ 격자 모양의 마을이 있다. 어느 날 세상에 좀비 바이러스가 창궐하여 바이러스가 빠르게 퍼져나가버린다. 바이러스에 대해 조사한 결과 세 종류의 바이러스가 존재했으며 각각 $1$번, $2$번, $3$번으로 번호를 매겼다.
#
# 바이러스의 특징은 다음과 같다.
#
#  $1$번과 $2$번 바이러스는 치사율은 낮지만 전염성이 강해 상하좌우에 인접해 있는 마을로 동시에 퍼져나가며 한 마을을 완전히 감염시키는 데 1시간 걸린다.
# 마을이 완전히 감염되어야 다른 마을로 퍼져나갈 수 있으며 다른 바이러스가 완전히 감염시킨 마을은 침범하지 않는다.
# 마을이 한 바이러스에 완전히 감염되기 전에 다른 종류의 바이러스가 마을에 도착하면 $3$번 바이러스가 만들어진다.
#  $3$번 바이러스는 치사율이 높은 만큼 전염성이 약해 감염된 마을에서 더 이상 퍼지지 않는다.
# 치료제를 갖고 있는 마을은 감염시킬 수 없다.
#
#
#  $1$번 바이러스와 $2$번 바이러스에 감염된 마을이 나와버렸다. 바이러스가 퍼질 수 있는 대로 퍼졌을 때 $1$번, $2$번, $3$번 바이러스에 감염된 마을이 각각 몇 개일지 구해보자.
#
# 입력
# 첫째 줄에 $N$($2≤N≤1\,000$)과 $M$($2≤M≤1\,000$)이 주어진다.
#
# 둘째 줄부터 $N$개의 줄에 걸쳐 마을의 상태가 $M$개 주어진다. 마을의 상태는 다음과 같이 이루어져 있다.
#
#  $-1$: 치료제를 가진 마을
#  $0$: 아직 감염되지 않은 마을
#  $1$: $1$번 바이러스에 감염된 마을
#  $2$: $2$번 바이러스에 감염된 마을
#  $1$번 바이러스와 $2$번 바이러스에 감염된 마을은 각각 하나씩만 주어진다.
#
# 출력
#  $1$번, $2$번, $3$번 바이러스에 감염된 마을의 수를 공백으로 구분하여 한 줄에 출력한다.
from collections import deque
n, m=map(int, input().split())
grid=[list(map(int, input().split())) for _ in range(n)]
one, two=deque(), deque()
for i in range(n):
    for j in range(m):
        if grid[i][j]==1:
            one.append((i, j))
        if grid[i][j]==2:
            two.append((i, j))
dy, dx=[0, 1, 0, -1], [1, 0, -1, 0]
cnt=[len(one), len(two), 0]
def bfs():
    set1, set2, set3=set(), set(), set()
    while one:
        y, x=one.popleft()
        for i in range(4):
            ny, nx=y+dy[i], x+dx[i]
            if 0<=ny<n and 0<=nx<m and grid[ny][nx]==0:
                set1.add((ny, nx))
    while two:
        y, x=two.popleft()
        for i in range(4):
            ny, nx=y+dy[i], x+dx[i]
            if 0<=ny<n and 0<=nx<m and grid[ny][nx]==0:
                set2.add((ny, nx))
    set3=set1&set2
    for y, x in set3:
        grid[y][x]=3
        cnt[2]+=1
    for y, x in set1-set3:
        grid[y][x]=1
        one.append((y, x))
        cnt[0]+=1
    for y, x in set2-set3:
        grid[y][x]=2
        two.append((y, x))
        cnt[1]+=1
while one or two:
    bfs()
print(*cnt)
