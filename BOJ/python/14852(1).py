# 문제
# 2×N 크기의 벽을 2×1, 1×2, 1×1 크기의 타일로 채우는 경우의 수를 구해보자.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 1,000,000)이 주어진다.
#
# 출력
# 첫째 줄에 경우의 수를 1,000,000,007로 나눈 나머지를 출력한다.
n=int(input())
dp=[0 for _ in range(n+2)]
dp[0]=1
dp[1]=2
dp[2]=7
if n<=2:
    print(dp[n])
    quit()
for i in range(3, n+1):
    dp[i]=(dp[i-1]*3+dp[i-2]-dp[i-3])%1000000007
print(dp[n]%1000000007)
