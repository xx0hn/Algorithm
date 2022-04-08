# 강력한 폭발
# 0, 1로 구성된 n * n 크기의 격자판이 주어집니다. 1은 해당 위치에 폭탄이 놓이게 됨을 의미합니다. 1이 써있는 위치에 각각 다음 3가지 중 하나의 폭탄을 선택하여 초토화시킬 지역의 수를 최대화 하려고 합니다. 각 폭탄은 폭탄위치를 포함하여 파란색으로 표시된 영역을 초토화시키게 됩니다.



# 다음과 같이 폭탄을 놓아야 하는 위치가 2곳인 경우를 생각해봅시다.



# 만약 다음과 같이 폭탄을 놓게 되면 총 7곳이 초토화됩니다.



# 하지만 다음과 같이 폭탄을 놓게 되면, 총 9곳이 초토화됩니다.



# 초기 격자판의 상태와 폭탄을 놓아야 할 위치들이 주어졌을 때, 가장 많이 초토화시킬 수 있는 영역의 수를 구하는 프로그램을 작성해보세요.

# 입력 형식
# 첫 번째 줄에는 격자의 크기를 나타내는 n이 주어집니다.

# 두 번째 줄 부터는 n개의 줄에 걸쳐 각 행에 해당하는 n개의 숫자가 공백을 사이에 두고 주어집니다. 각 숫자는 0, 1 중 하나이며 1은 폭탄을 놓아야 하는 위치임을 의미합니다.

# 1 ≤ n ≤ 20

# 1 ≤ 폭탄을 놓아야 하는 위치의 수 ≤ 10

# 출력 형식
# 가장 많이 폭발에 영향을 받을 수 있는 영역의 수를 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 4
# 0 0 0 0
# 0 0 1 0
# 0 1 0 0
# 0 0 0 0
# 출력:

# 9
# 예제2
# 입력:

# 4
# 0 1 0 0
# 0 1 0 0
# 0 1 0 0
# 0 1 0 0
# 출력:

# 12
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
import copy
n=int(input())
grid=[list(map(int, input().split())) for _ in range(n)]
bombs=[
    [[-2, -1, 1, 2], [0, 0, 0, 0]],
    [[-1, 0, 1, 0], [0, 1, 0, -1]],
    [[-1, -1, 1, 1], [-1, 1, 1, -1]]]
idx=[]
for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            idx.append([i, j])
answers=[]
def expld(y, x, bomb, g):
    for i in range(4):
        ny, nx=y+bomb[0][i], x+bomb[1][i]
        if 0<=ny<n and 0<=nx<n:
            g[ny][nx]=1
    return g
def get_range(cur, grid):
    if cur==len(idx):
        cnt=0
        for i in range(n):
            for j in range(n):
                cnt+=grid[i][j]
        answers.append(cnt)
        return
    for i in range(3):
        tmp=copy.deepcopy(grid)
        nxt_grid=expld(idx[cur][0], idx[cur][1], bombs[i], tmp)
        get_range(cur+1, nxt_grid)
get_range(0, grid)
print(max(answers))
