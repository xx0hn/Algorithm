# 문제
# 수빈이는 강호와 함께 스타크래프트 게임을 하고 있다. 수빈이는 뮤탈리스크 1개가 남아있고, 강호는 SCV N개가 남아있다.
#
# 각각의 SCV는 남아있는 체력이 주어져있으며, 뮤탈리스크를 공격할 수는 없다. 즉, 이 게임은 수빈이가 이겼다는 것이다.
#
# 뮤탈리스크가 공격을 할 때, 한 번에 세 개의 SCV를 공격할 수 있다.
#
# 첫 번째로 공격받는 SCV는 체력 9를 잃는다.
# 두 번째로 공격받는 SCV는 체력 3을 잃는다.
# 세 번째로 공격받는 SCV는 체력 1을 잃는다.
# SCV의 체력이 0 또는 그 이하가 되어버리면, SCV는 그 즉시 파괴된다. 한 번의 공격에서 같은 SCV를 여러 번 공격할 수는 없다.
#
# 남아있는 SCV의 체력이 주어졌을 때, 모든 SCV를 파괴하기 위해 공격해야 하는 횟수의 최솟값을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 SCV의 수 N (1 ≤ N ≤ 3)이 주어진다. 둘째 줄에는 SCV N개의 체력이 주어진다. 체력은 60보다 작거나 같은 자연수이다.
#
# 출력
# 첫째 줄에 모든 SCV를 파괴하기 위한 공격 횟수의 최솟값을 출력한다.
import itertools
import sys
n=int(input())
scv=list(map(int, input().split()))
if n<3:
    scv+=[0]*(3-n)
attacks=[9, 3, 1]
dp=[[[-1 for _ in range(61)] for _ in range(61)] for _ in range(61)]
def hp_update(a, b, c):
    if a<0:
        return hp_update(0, b, c)
    if b<0:
        return hp_update(a, 0, c)
    if c<0:
        return hp_update(a, b, 0)
    if not a and not b and not c:
        return 0
    if dp[a][b][c]!=-1:
        return dp[a][b][c]
    dp[a][b][c]=sys.maxsize
    for damage in list(itertools.permutations(attacks)):
        dp[a][b][c]=min(dp[a][b][c], hp_update(a-damage[0], b-damage[1], c-damage[2]))
    dp[a][b][c]+=1
    return dp[a][b][c]
print(hp_update(scv[0], scv[1], scv[2]))
