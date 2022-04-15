# 마을 구분하기
# n * n크기의 이차원 영역에 사람 혹은 벽이 놓여져있습니다. 이 때 상하좌우의 인접한 영역에 있는 사람들은 같은 마을에 있는 것으로 간주한다고 합니다. 예를 들어 <그림 1> 같이 사람과 벽이 배치되어 있는 경우, 그림 안의 점선과 같이 마을을 나눌 수 있습니다. 이 때 총 마을의 개수와 같은 마을에 있는 사람의 수를 오름차순으로 정렬하여 출력하는 코드를 작성해보세요.



# 입력 형식
# 첫 번째 줄에는 n이 주어지고,

# 두 번째 줄부터 (n+1)번째 줄까지는 각 행에 사람이 있는 경우 1, 벽이 있는 경우 0으로 입력이 공백을 사이에 두고 주어집니다.

# 5 ≤ n ≤ 25
# 출력 형식
# 첫 번째 줄에는 총 마을의 개수를 출력하고,

# 그 다음 줄부터 각 줄에는 각 마을 내 사람의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하세요.

# 입출력 예제
# 예제1
# 입력:

# 5
# 1 0 1 1 1
# 1 0 0 0 0
# 0 0 0 1 1
# 1 1 0 1 1
# 1 1 0 1 1
# 출력:

# 4
# 2
# 3
# 4
# 6
# 예제2
# 입력:

# 5
# 0 1 0 0 1
# 0 1 0 1 1
# 0 1 0 0 1
# 0 1 1 1 1
# 1 0 0 0 0
# 출력:

# 2
# 1
# 11
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
n=int(input())
grid=[list(map(int, input().split())) for _ in range(n)]
dy, dx=[0, 1, 0 , -1], [1, 0, -1, 0]
visited=[[False for _ in range(n)] for _ in range(n)]
cnt=0
def dfs(y, x):
    global cnt
    for i in range(4):
        ny, nx=y+dy[i], x+dx[i]
        if 0<=ny<n and 0<=nx<n and grid[ny][nx]==1 and not visited[ny][nx]:
            visited[ny][nx]=True
            cnt+=1
            dfs(ny, nx)
answer=0
answers=[]
for i in range(n):
    for j in range(n):
        if grid[i][j]==1 and not visited[i][j]:
            answer+=1
            dfs(i, j)
            if cnt==0:
                cnt+=1
            answers.append(cnt)
            cnt=0
print(answer)
answers.sort()
for i in range(answer):
    print(answers[i])
