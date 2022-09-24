t = int(input())
for _ in range(t):
	n, k = map(int, input().split())
	grid = [list(map(int, input().split())) for _ in range(n)]
	answer = 1e9
	for i in range(n-k+1):
		for j in range(n-k+1):
			ans = 0
			for r in range(i, i+k):
				ans += sum(grid[r][j:j+k])
			answer = min(answer, ans)
	print(answer)
