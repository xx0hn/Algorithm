# 문제
# 마법사 상어는 파이어볼, 토네이도, 파이어스톰, 물복사버그 마법을 할 수 있다. 오늘 새로 배운 마법은 비바라기이다. 비바라기를 시전하면 하늘에 비구름을 만들 수 있다. 오늘은 비바라기를 크기가 N×N인 격자에서 연습하려고 한다. 격자의 각 칸에는 바구니가 하나 있고, 바구니는 칸 전체를 차지한다. 바구니에 저장할 수 있는 물의 양에는 제한이 없다. (r, c)는 격자의 r행 c열에 있는 바구니를 의미하고, A[r][c]는 (r, c)에 있는 바구니에 저장되어 있는 물의 양을 의미한다.
#
# 격자의 가장 왼쪽 윗 칸은 (1, 1)이고, 가장 오른쪽 아랫 칸은 (N, N)이다. 마법사 상어는 연습을 위해 1번 행과 N번 행을 연결했고, 1번 열과 N번 열도 연결했다. 즉, N번 행의 아래에는 1번 행이, 1번 행의 위에는 N번 행이 있고, 1번 열의 왼쪽에는 N번 열이, N번 열의 오른쪽에는 1번 열이 있다.
#
# 비바라기를 시전하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생긴다. 구름은 칸 전체를 차지한다. 이제 구름에 이동을 M번 명령하려고 한다. i번째 이동 명령은 방향 di과 거리 si로 이루어져 있다. 방향은 총 8개의 방향이 있으며, 8개의 정수로 표현한다. 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 이다. 이동을 명령하면 다음이 순서대로 진행된다.
#
# 모든 구름이 di 방향으로 si칸 이동한다.
# 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
# 구름이 모두 사라진다.
# 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
# 이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
# 예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고, (N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다.
# 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
# M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합을 구해보자.
#
# 입력
# 첫째 줄에 N, M이 주어진다.
#
# 둘째 줄부터 N개의 줄에는 N개의 정수가 주어진다. r번째 행의 c번째 정수는 A[r][c]를 의미한다.
#
# 다음 M개의 줄에는 이동의 정보 di, si가 순서대로 한 줄에 하나씩 주어진다.
#
# 출력
# 첫째 줄에 M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합을 출력한다.
#
# 제한
# 2 ≤ N ≤ 50
# 1 ≤ M ≤ 100
# 0 ≤ A[r][c] ≤ 100
# 1 ≤ di ≤ 8
# 1 ≤ si ≤ 50
import copy
n, m=map(int, input().split())
grid=[list(map(int, input().split())) for _ in range(n)]
commands=[list(map(int, input().split())) for _ in range(m)]
dy=[0, 0, -1, -1, -1, 0, 1, 1, 1]
dx=[0, -1, -1, 0, 1, 1, 1, 0, -1]
clouds=[[False for _ in range(n)] for _ in range(n)]
clouds[n-1][0], clouds[n-1][1], clouds[n-2][0], clouds[n-2][1]=True, True, True, True
def make_clouds():
    for i in range(n):
        for j in range(n):
            if not clouds[i][j] and grid[i][j]>=2:
                clouds[i][j]=True
                grid[i][j]-=2
            elif clouds[i][j]:
                clouds[i][j]=False
def move_clouds(d, s):
    global clouds
    tmp=[[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if clouds[i][j]:
                tmp[(i+s*dy[d])%n][(j+s*dx[d])%n]=True
    clouds=copy.deepcopy(tmp)
def pouring():
    for i in range(n):
        for j in range(n):
            if clouds[i][j]:
                grid[i][j]+=1
    for i in range(n):
        for j in range(n):
            if clouds[i][j]:
                for l in range(2, 9, 2):
                    if 0<=i+dy[l]<n and 0<=j+dx[l]<n and grid[i+dy[l]][j+dx[l]]>0:
                        grid[i][j]+=1
def get_sum():
    result=0
    for i in range(n):
        result+=sum(grid[i])
    return result
for i in range(m):
    move_clouds(commands[i][0], commands[i][1])
    pouring()
    make_clouds()
print(get_sum())
