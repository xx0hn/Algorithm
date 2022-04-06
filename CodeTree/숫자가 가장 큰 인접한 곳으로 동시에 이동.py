# 숫자가 가장 큰 인접한 곳으로 동시에 이동
# 1 ~ 100 사이의 숫자로 이루어진 n * n 크기의 격자판 정보가 주어집니다. 이때 m개 구슬이 서로 다른 위치에서 시작하여 1초에 한 번씩 상하좌우로 인접한 곳에 있는 숫자들 중 가장 큰 값이 적혀있는 숫자가 있는 위치로 동시에 이동합니다. 만약 그러한 위치가 여러개 있는 경우, 상하좌우 방향 순서대로 우선순위를 매겨 가능한 곳 중 우선순위가 더 높은 곳으로 이동합니다. 단, 이때 격자를 벗어나서는 안됩니다.

# 예를 들어, 다음 그림의 경우를 살펴봅시다. 처음에 3개의 구슬이 각각 2행 2열, 3행 4열, 4행 2열에 놓여있었다고 생각해봅시다.



# 이 그림에서 1초 뒤의 모습은 다음과 같습니다.



# 이때, 각 구슬이 움직인 이후의 위치가 동일하지 않다면 구슬은 절대 서로 충돌하지 않습니다.

# 따라서 위의 경우에서 1초가 더 흐른 후의 모습은 다음과 같습니다.



# 하지만, 이동한 이후 2개 이상의 구슬 위치가 동일하다면, 해당 위치에 있는 구슬들은 전부 사라지게 됩니다.

# 따라서 위의 경우에서 1초가 더 흐른 후의 모습은 다음과 같습니다.



# 격자판의 정보와 초기 구슬들의 위치가 주어졌을 때, t초 후 남아있는 구슬의 수를 출력하는 프로그램을 작성해보세요.

# 입력 형식
# 첫 번째 줄에는 격자의 크기를 나타내는 n과 구슬의 개수를 나타내는 m, 그리고 시간을 나타내는 t값이 각각 공백을 사이에 두고 주어집니다.

# 두 번째 줄 부터는 n개의 줄에 걸쳐 각 행에 해당하는 n개의 숫자가 공백을 사이에 두고 주어집니다.

# 그 다음 줄 부터는 m개의 줄에 걸쳐 각 구슬의 시작 위치를 나타내는 r, c 값이 각각 공백을 사이에 두고 주어집니다. r, c는 r행 c열에서 시작함을 의미하며, 모든 구슬의 시작 위치는 다르다고 가정해도 좋습니다. (1 ≤ r, c ≤ n)

# 2 ≤ n ≤ 20

# 1 ≤ m ≤ n * n

# 1 ≤ t ≤ 100

# 출력 형식
# t초 이후 격자판 이후 남아있는 구슬의 수를 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 4 3 1
# 1 2 2 3
# 3 5 10 15
# 3 8 11 2
# 4 5 4 4
# 2 2
# 3 4
# 4 2
# 출력:

# 3
# 예제2
# 입력:

# 4 3 3
# 1 2 2 3
# 3 5 10 15
# 3 8 11 2
# 4 5 4 4
# 2 2
# 3 4
# 4 2
# 출력:

# 1
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
import copy
n, m, t=map(int, input().split())
grid=[list(map(int, input().split())) for _ in range(n)]
cnt=[[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b=map(int, input().split())
    cnt[a-1][b-1]=1
nxt_cnt=[[0 for _ in range(n)] for _ in range(n)]
def move():
    global cnt
    dy, dx=[-1, 1, 0, 0], [0, 0, -1, 1]
    nxt_cnt=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if cnt[i][j]==1:
                mx, idx=-1, [0, 0]
                for l in range(4):
                    ny, nx=i+dy[l], j+dx[l]
                    if 0<=ny<n and 0<=nx<n and grid[ny][nx]>mx:
                        mx=grid[ny][nx]
                        idx=[ny, nx]
                nxt_cnt[idx[0]][idx[1]]+=1
    cnt=copy.deepcopy(nxt_cnt)
def rmv():
    for i in range(n):
        for j in range(n):
            if cnt[i][j]>=2:
                cnt[i][j]=0
for _ in range(t):
    move()
    rmv()
answer=0
for i in range(n):
    for j in range(n):
        answer+=cnt[i][j]
print(answer)
