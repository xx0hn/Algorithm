# 트로미노
# n * m크기의 이차원 영역의 각 위치에 자연수가 하나씩 적혀있습니다. 이 때 아래의 그림에 주어진 2가지 종류의 블럭 중 한 개를 블럭이 격자를 벗어나지 않도록 적당히 올려놓아 블럭이 놓인 칸 안에 적힌 숫자의 합이 최대가 될 때의 결과를 출력하는 프로그램을 작성해보세요. 단, 주어진 블럭은 자유롭게 회전하거나 뒤집을 수 있습니다.



# 입력 형식
# 첫 번째 줄에는 n과 m이 공백을 사이에 두고 주어지고, 두 번째 줄부터 (n+1)번째 줄까지는 각 행의 숫자가 공백을 사이에 두고 주어집니다.

# 3 ≤ n, m ≤ 200

# 1 ≤ 자연수 ≤ 1,000

# 출력 형식
# 블럭 안에 적힌 숫자합의 최대값을 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 3 3
# 1 2 3
# 3 2 1
# 3 1 1
# 출력:

# 8
# 예제2
# 입력:

# 4 5
# 6 5 4 3 1
# 3 4 4 14 1
# 6 1 3 15 5
# 3 5 1 16 3
# 출력:

# 45
# 예제 설명
# 2번째 예제는 다음과 같이 놓았을 때 합이 최대가 됩니다.



# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
n, m=map(int, input().split())
grid=[]
for _ in range(n):
    grid.append(list(map(int, input().split())))
dn=[[[-1, 0], [0, 1]], [[0, 1], [1, 0]], [[0, -1], [1, 0]], [[0, -1], [-1, 0]]]
dw=[[[0, 1], [0, 2]], [[1, 0], [2, 0]]]
def chk_n(y, x):
    result=[grid[y][x]]*4
    for i in range(4):
        for j in range(2):
            ny=y+dn[i][j][0]
            nx=x+dn[i][j][1]
            if 0<=ny<n and 0<=nx<m:
                result[i]+=grid[ny][nx]
            else:
                result[i]=0
                break
    return max(result)
def chk_w(y, x):
    result=[grid[y][x]]*2
    for i in range(2):
        for j in range(2):
            ny=y+dw[i][j][0]
            nx=x+dw[i][j][1]
            if 0<=ny<n and 0<=nx<m:
                result[i]+=grid[ny][nx]
            else:
                result[i]=0
                break
    return max(result)
results=[]
for i in range(n):
    for j in range(m):
        results.append(chk_n(i, j))
        results.append(chk_w(i, j))
print(max(results))
