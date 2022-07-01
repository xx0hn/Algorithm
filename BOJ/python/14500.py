# 문제
# 폴리오미노란 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음과 같은 조건을 만족해야 한다.
#
# 정사각형은 서로 겹치면 안 된다.
# 도형은 모두 연결되어 있어야 한다.
# 정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.
# 정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 하며, 다음과 같은 5가지가 있다.
#
#
#
# 아름이는 크기가 N×M인 종이 위에 테트로미노 하나를 놓으려고 한다. 종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 정수가 하나 쓰여 있다.
#
# 테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.
#
# 테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.
#
# 입력
# 첫째 줄에 종이의 세로 크기 N과 가로 크기 M이 주어진다. (4 ≤ N, M ≤ 500)
#
# 둘째 줄부터 N개의 줄에 종이에 쓰여 있는 수가 주어진다. i번째 줄의 j번째 수는 위에서부터 i번째 칸, 왼쪽에서부터 j번째 칸에 쓰여 있는 수이다. 입력으로 주어지는 수는 1,000을 넘지 않는 자연수이다.
#
# 출력
# 첫째 줄에 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값을 출력한다.
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
def chk_one(y, x):
    result = 0
    if 0 <= x+3 < m:
        result = max(result, sum(grid[y][x:x+4]))
    if 0 <= y+3 < n:
        tmp = 0
        for i in range(y, y+4):
            tmp += grid[i][x]
        result = max(result, tmp)
    return result
def chk_two(y, x):
    result = 0
    if 0 <= y+1 < n and 0 <= x+1 < m:
        result += (grid[y][x] + grid[y+1][x] + grid[y][x+1] + grid[y+1][x+1])
    return result
def chk_three(y, x):
    result = 0
    if 0 <= y+2 < n and 0 <= x+1 < m:
        tmp1 = 0
        for i in range(y, y+3):
            tmp1 += grid[i][x]
        tmp1 += grid[y+2][x+1]
        tmp2 = 0
        for i in range(y, y+3):
            tmp2 += grid[i][x+1]
        tmp2 += grid[y][x]
        tmp3 = 0
        for i in range(y, y+3):
            tmp3 += grid[i][x]
        tmp3 += grid[y][x+1]
        result = max(result, tmp1, tmp2, tmp3)
    if 0 <= y+1 < n and 0 <= x+2 < m:
        tmp1 = 0
        tmp1 += sum(grid[y][x:x+3])
        tmp1 += grid[y+1][x]
        tmp2 = 0
        tmp2 += sum(grid[y][x:x+3])
        tmp2 += grid[y+1][x+2]
        tmp3 = 0
        tmp3 += sum(grid[y+1][x:x+3])
        tmp3 += grid[y][x]
        result = max(result, tmp1, tmp2, tmp3)
    if 0 <= y+1 < n and 0 <= x-2 < m:
        tmp = 0
        tmp += sum(grid[y+1][x-2:x+1])
        tmp += grid[y][x]
        result = max(result, tmp)
    if 0 <= y+2 < n and 0 <= x-1 < m:
        tmp = 0
        for i in range(y, y+3):
            tmp += grid[i][x]
        tmp += grid[y+2][x-1]
        result = max(result, tmp)
    if 0 <= y-1 < n and 0 <= x+2 < m:
        tmp = 0
        tmp += sum(grid[y][x:x+3])
        tmp += grid[y-1][x+2]
        result = max(result, tmp)
    return result
def chk_four(y, x):
    result = 0
    if 0 <= y+2 < n and 0 <= x+1 < m:
        tmp = (grid[y][x] + grid[y+1][x] + grid[y+1][x+1] + grid[y+2][x+1])
        result = max(result, tmp)
    if 0 <= y+1 < n and 0 <= x-1 < m and 0 <= x+1 < m:
        tmp = (grid[y][x] + grid[y][x+1] + grid[y+1][x] + grid[y+1][x-1])
        result = max(result, tmp)
    if 0 <= y+2 < n and 0 <= x-1 < m:
        tmp = (grid[y][x] + grid[y+1][x] + grid[y+1][x-1] + grid[y+2][x-1])
        result = max(result, tmp)
    if 0 <= y+1 < n and 0 <= x+2 < m:
        tmp = (grid[y][x] + grid[y][x+1] + grid[y+1][x+1] + grid[y+1][x+2])
        result = max(result, tmp)
    return result
def chk_five(y, x):
    result = 0
    if 0 <= y+1 < n and 0 <= x-1 < m and 0 <= x+1 < m:
        tmp1 = (grid[y][x] + grid[y+1][x] + grid[y][x-1] + grid[y][x+1])
        tmp2 = (grid[y][x] + grid[y+1][x] + grid[y+1][x-1] + grid[y+1][x+1])
        result = max(result, tmp1, tmp2)
    if 0 <= y+2 < n and 0 <= x+1 < m:
        tmp = 0
        for i in range(y, y+3):
            tmp += grid[i][x]
        tmp += grid[y+1][x+1]
        result = max(result, tmp)
    if 0 <= y+2 < n and 0 <= x-1 < m:
        tmp = 0
        for i in range(y, y+3):
            tmp += grid[i][x]
        tmp += grid[y+1][x-1]
        result = max(result, tmp)
    return result
answer = 0
for i in range(n):
    for j in range(m):
        answer = max(answer, chk_one(i, j), chk_two(i, j), chk_three(i, j), chk_four(i, j), chk_five(i, j))
print(answer)
