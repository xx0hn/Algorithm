# 문제
# n×m의 0, 1로 된 배열이 있다. 이 배열에서 1로 된 가장 큰 정사각형의 크기를 구하는 프로그램을 작성하시오.
#
# 0	1	0	0
# 0	1	1	1
# 1	1	1	0
# 0	0	1	0
# 위와 같은 예제에서는 가운데의 2×2 배열이 가장 큰 정사각형이다.
#
# 입력
# 첫째 줄에 n, m(1 ≤ n, m ≤ 1,000)이 주어진다. 다음 n개의 줄에는 m개의 숫자로 배열이 주어진다.
#
# 출력
# 첫째 줄에 가장 큰 정사각형의 넓이를 출력한다.
n, m = map(int, input().split())
grid = [list(str(input())) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    dp[i][0] = int(grid[i][0])
for i in range(m):
    dp[0][i] = int(grid[0][i])
for i in range(1, n):
    for j in range(1, m):
        if grid[i][j] == '1':
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1
answer = 0
for i in range(n):
    answer = max(answer, max(dp[i]))
print(answer**2)
