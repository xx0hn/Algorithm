# 최적의 십자 모양 폭발
# 1~100 사이의 숫자로 구성된 n * n 크기의 격자판이 주어집니다. 이때 특정 위치를 선택하면, 그 위치를 중심으로 십자 모양으로 폭탄이 터지게 됩니다. 십자 모양의 크기는 선택된 위치에 적혀있는 숫자로 정해지며, 터진 이후에는 중력에 의해 숫자들이 아래로 떨어지게 됩니다.

# 십자 모양의 크기는 선택된 숫자에 비례하여 커집니다. 선택된 숫자가 1인 경우에는 자기 자신만 터지게 되고, 선택한 숫자가 2인 경우에는 자신을 포함하여 인접한 4개의 격자 역시 터지게 되며, 3인 경우에는 자신을 제외한 상하좌우 방향으로 각각 2개씩이 더 터지게 됩니다. 숫자가 4 이상인 경우에도 마찬가지의 규칙에 따라 해당 범위만큼 터지게 됩니다.



# 예를 들어 다음 위치를 선택하게 되면, 폭탄이 터지고 중력이 작용한 이후의 결과가 다음과 같이 나타나게 됩니다.



# 또 다른 예로 다음 위치를 선택하게 되었을 때 결과는 다음과 같습니다.



# 만약 다음과 같이 폭탄이 터져야 하는 범위가 격자 판을 벗어나게 되더라도, 격자 안에서만 폭탄이 터집니다.



# 최적의 십자 모양 폭발이란, 특정 위치를 선택하여 폭탄이 터진 뒤 중력이 작용한 이후에 상하좌우로 인접한 격자끼리 적혀있는 숫자가 동일한 쌍의 수가 최대가 되도록 하는 폭발을 의미합니다.

# 만약 3행 3열을 중심으로 터뜨리게 된다면, 인접한 곳끼리 숫자가 동일한 쌍의 수가 총 2개가 됩니다.



# 하지만 만약 3행 2열을 중심으로 터뜨리게 된다면, 조건을 만족하는 쌍의 수는 5개로 최대가 됩니다.


# 초기 격자판의 상태가 주어졌을 때 폭탄이 터질 중심 위치를 적절하게 골라, 폭탄이 터진 뒤 중력이 작용하고 나서 조건을 만족하는 쌍의 개수가 최대가 되도록 하는 프로그램을 작성해보세요.

# 입력 형식
# 첫 번째 줄에는 격자의 크기를 나타내는 n이 주어집니다.

# 두 번째 줄 부터는 n개의 줄에 걸쳐 각 행에 해당하는 n개의 숫자가 공백을 사이에 두고 주어집니다.

# 1 ≤ n ≤ 50
# 출력 형식
# 터질 폭탄의 중심 위치를 적절하게 골랐을 때, 폭탄이 터지고 나서 중력이 작용한 뒤 얻을 수 있는 최대 쌍의 수를 출력합니다. 폭탄을 터뜨리지 않았을 때 조건을 만족하는 쌍의 수가 최대라 하더라도, 폭탄이 꼭 한번 터졌을 때를 고려해야 하는 문제임에 유의합니다.

# 입출력 예제
# 예제1
# 입력:

# 4
# 1 2 4 3
# 3 2 2 3
# 3 1 6 2
# 4 5 4 4
# 출력:

# 5
# 예제2
# 입력:

# 3
# 1 2 1
# 4 5 6
# 1 8 1
# 출력:

# 2
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
import copy
n=int(input())
grid=[list(map(int, input().split())) for _ in range(n)]
def chk(results):
    result=0
    for i in range(n):
        for j in range(1, n):
            if (results[i][j-1]!=0 and results[i][j]!=0) and (results[i][j-1]==results[i][j]):
                result+=1
            if (results[j-1][i]!=0 and results[j][i]!=0) and (results[j-1][i]==results[j][i]):
                result+=1
    return result
def bomb(y, x):
    test=copy.deepcopy(grid)
    area=test[y][x]
    tmp=[[] for _ in range(n)]
    dy, dx=[0, -1, 0, 1], [1, 0, -1, 0]
    for i in range(4):
        for j in range(area):
            ny, nx=y+dy[i]*j, x+dx[i]*j
            if 0<=ny<n and 0<=nx<n:
                test[ny][nx]=0
    for i in range(n):
        for j in range(n):
            if test[j][i]!=0:
                tmp[i].append(test[j][i])
    for i in range(n):
        tmp[i]=([0]*(n-len(tmp[i])))+tmp[i]
    results=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            results[i][j]=tmp[j][i]
    return chk(results)
answers=[]
for i in range(n):
    for j in range(n):
        answers.append(bomb(i, j))
print(max(answers))
