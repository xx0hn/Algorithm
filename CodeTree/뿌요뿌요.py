# 뿌요뿌요
# n * n 크기의 격자에 1에서 100 사이의 숫자가 각 칸에 하나씩 주어집니다. 이때 상하좌우로 인접한 칸끼리 같은 숫자로 이루어져 있는 경우 하나의 블럭으로 생각하며, 블럭을 이루고 있는 칸의 수가 4개 이상인 경우 해당 블럭은 터지게 됩니다.

# 초기 상태가 주어졌을 때 터지게 되는 블럭의 수와, 최대 블럭의 크기를 구하는 프로그램을 작성해보세요.

# 입력 형식
# 첫 번째 줄에는 격자의 크기를 나타내는 n이 주어집니다.

# 두 번째 줄부터는 n개의 줄에 걸쳐 각 행에 해당하는 n개의 숫자가 순서대로 공백을 사이에 두고 주어집니다.

# 1 ≤ n ≤ 100
# 1 ≤ 주어지는 숫자 ≤ 100
# 출력 형식
# 터지게 되는 블럭의 수와 최대 블럭의 크기를 공백을 사이에 두고 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 3
# 1 1 1
# 2 1 2
# 1 1 1
# 출력:

# 1 7
# 예제2
# 입력:

# 3
# 1 2 2
# 1 2 2
# 1 1 1
# 출력:

# 2 5
# 예제3
# 입력:

# 3
# 1 2 4
# 1 2 2
# 3 1 1
# 출력:

# 0 3
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
n=int(input())
grid=[list(map(int, input().split())) for _ in range(n)]
visited=[[False for _ in range(n)] for _ in range(n)]
dy, dx=[0, 1, 0, -1], [1, 0, -1, 0]
cnt=0
answer=1
def dfs(y, x):
    global answer
    for i in range(4):
        ny, nx=y+dy[i], x+dx[i]
        if 0<=ny<n and 0<=nx<n and grid[y][x]==grid[ny][nx] and not visited[ny][nx]:
            visited[ny][nx]=True
            answer+=1
            dfs(ny, nx)
answers=0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j]=True
            dfs(i, j)
            if answer>=4:
                cnt+=1
            answers=max(answers, answer)
            answer=1
print(cnt, answers)
