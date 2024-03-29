# 문제
# 0과 1로 구성된 이진수가 있다. 이 이진수에서 0을 10으로, 1을 01로 동시에 치환하면 길이가 두 배인 이진수를 얻을 수 있다. 이러한 이진수들을 차례로 나열하면 하나의 이진수 수열이 된다. 편의상 시작 수는 1이라고 하자. 처음 몇 개의 이진수들을 구해 보면,
#
# 1 → 01 → 1001 → 01101001 → …
#
# 이 된다.
#
# N이 주어졌을 때, N번째 이진수에서 연속된 0들의 그룹이 몇 개나 있는지 알아내는 프로그램을 작성하시오. N=4일 경우의 이진수는 01101001이고, 따라서 이 안에는 연속된 0들이 세 그룹 있게 된다.
#
# 입력
# 첫째 줄에 정수 N(1 ≤ N ≤ 1,000)이 주어진다.
#
# 출력
# 첫째 줄에 답을 출력한다.
n=int(input())
dp=[0 for _ in range(n+1)]
for i in range(2, n+1):
    if i%2:
        dp[i]=dp[i-1]*2-1
    else:
        dp[i]=dp[i-1]*2+1
print(dp[n])
