# 단 한 번의 2048 시도
# 2048게임은 4 * 4 격자 안에서 이루어지는 게임입니다. 이 2048 게임에서는 상하좌우 중 한 방향을 정하게 되면, 모든 숫자들이 해당 방향으로 전부 밀리게 됩니다.

# 예를 들어 다음 판에서 밑으로 방향을 정하게 되면, 다음과 같이 아래로 중력이 작용한 이후의 결과를 얻게 됩니다.



# 하지만 2048 게임에서는 같은 숫자끼리 만나게 되는 경우 두 숫자가 합쳐지게 됩니다. 다음의 경우 아래로 움직이는 예를 보면 숫자 2 두 개가 합쳐서 숫자 4가 됩니다.



# 또한, 단 한 번의 중력작용으로 이미 합쳐진 숫자가 연쇄적으로 합쳐지진 않습니다. 다음의 경우 아래로 움직이는 예를 보면 숫자 2 두 개가 이미 한번 합쳐져 4가 되었기 때문에, 위의 4와 다시 합쳐지진 않습니다.


# 그리고 세 개 이상의 같은 숫자가 중력작용 방향으로 놓여 있으면, 중력에 의해 부딪히게 될 벽(바닥)에서 가까운 숫자부터 두 개씩만 합쳐집니다. 즉, 서너개 이상의 숫자가 하나로 합쳐질 순 없고 아래 예시처럼 바닥에 가까운 순서대로 한 쌍씩 짝을 이뤄 합쳐집니다. 다음 예시는 아래로 중력이 작용해서 숫자 2 네개가 4 두개로 합쳐진 것입니다.



# 2, 4, 8, 16 등 2의 거듭제곱꼴로 나타나는 2 이상 2048 이하의 숫자들로 구성된 4 * 4 격자 판이 주어졌을 때, 특정 방향으로 움직인 이후의 결과를 구하는 프로그램을 작성해보세요.

# 예를 들어 다음의 경우 오른쪽으로 이동하게 되면, 다음과 같은 결과를 얻게 됩니다.



# 입력 형식
# 첫 번째 줄부터 4번째 줄까지는 각각의 행에 놓여진 숫자 4개가 공백을 사이에 두고 주어집니다. 만약 숫자가 적혀있지 않는 경우에는 0이 주어집니다.

# 5번째 줄에는 움직일 방향을 나타내는 dir 값이 주어집니다. dir 값은 ‘L', ‘R’, ‘U’, 'D’ 중 하나이며, 각각 왼쪽 오른쪽 위 아래 방향으로 움직여야 함을 의미합니다.

# 출력 형식
# dir 방향으로 움직인 이후의 결과를 4개의 줄에 걸쳐 출력합니다. 각각의 줄에는 해당 행에 적혀있는 숫자 4개를 공백을 사이에 두고 출력하며, 만약 숫자가 적혀있지 않은 위치의 경우에는 0을 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 4 2 0 8
# 4 2 2 4
# 0 8 8 2
# 4 2 2 2
# R
# 출력:

# 0 4 2 8
# 0 4 4 4
# 0 0 16 2
# 0 4 2 4
# 예제2
# 입력:

# 4 2 0 8
# 4 2 2 4
# 0 8 8 2
# 4 2 2 2
# L
# 출력:

# 4 2 8 0
# 4 4 4 0
# 16 2 0 0
# 4 4 2 0
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
import copy
grid=[list(map(int, input().split())) for _ in range(4)]
dr=str(input())
def combine(dr):
    global grid
    grid=copy.deepcopy(move(dr))
    if dr=='L':
        for i in range(4):
            for j in range(1, 4):
                if grid[i][j]==grid[i][j-1]:
                    grid[i][j-1], grid[i][j]=grid[i][j]*2, 0
    if dr=='R':
        for i in range(4):
            for j in range(3, 0, -1):
                if grid[i][j]==grid[i][j-1]:
                    grid[i][j], grid[i][j-1]=grid[i][j]*2, 0
    if dr=='U':
        for i in range(4):
            for j in range(1, 4):
                if grid[j][i]==grid[j-1][i]:
                    grid[j-1][i], grid[j][i]=grid[j][i]*2, 0
    if dr=='D':
        for i in range(4):
            for j in range(3, 0, -1):
                if grid[j][i]==grid[j-1][i]:
                    grid[j][i], grid[j-1][i]=grid[j][i]*2, 0
def move(dr):
    tmp=[[] for _ in range(4)]
    if dr=='L' or dr=='R':
        for i in range(4):
            for j in range(4):
                if grid[i][j]!=0:
                    tmp[i].append(grid[i][j])
        if dr=='L':
            for i in range(4):
                tmp[i]+=[0]*(4-len(tmp[i]))
        if dr=='R':
            for i in range(4):
                tmp[i]=[0]*(4-len(tmp[i]))+tmp[i]
        return tmp
    if dr=='U' or dr=='D':
        for i in range(4):
            for j in range(4):
                if grid[j][i]!=0:
                    tmp[i].append(grid[j][i])
        if dr=='U':
            for i in range(4):
                tmp[i]+=[0]*(4-len(tmp[i]))
        if dr=='D':
            for i in range(4):
                tmp[i]=[0]*(4-len(tmp[i]))+tmp[i]
        result=[[0]*4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                result[i][j]=tmp[j][i]
        return result
combine(dr)
answer=copy.deepcopy(move(dr))
for i in range(4):
    print(*answer[i])
