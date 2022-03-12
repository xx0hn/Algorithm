# 문제
# 2×N 크기의 벽을 2×1, 1×2, 1×1 크기의 타일로 채우는 경우의 수를 구해보자.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 1,000,000)이 주어진다.
#
# 출력
# 첫째 줄에 경우의 수를 1,000,000,007로 나눈 나머지를 출력한다.
n=int(input())
dp=[0 for _ in range(n+1)]
dp_sum=[0 for _ in range(n+1)]
dp[0], dp[1]=1, 2
dp_sum[0]=1
dp_sum[1]=dp_sum[0]+dp[1]
if n<=1:
    print(dp[n])
    quit()
for i in range(2, n+1):
    dp[i]=(dp_sum[i-1]*2+dp[i-2])%1000000007
    dp_sum[i]=(dp_sum[i-1]+dp[i])%1000000007
print(dp[n]%1000000007)
